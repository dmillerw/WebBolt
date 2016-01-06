import threading
import Queue

import state
import gatt

import base_action

class ActionThread(threading.Thread):
    def __init__(self):
        super(ActionThread, self).__init__()
        self.alive = threading.Event()
        self.alive.set()
        self.queue = Queue.Queue()
        self.device = gatt.connect("20:C3:8F:F3:09:98")
        self.current_state = state.from_device(self.device)

    def run(self):
        while self.alive.isSet():
            try:
                if self.device.conn is not None:
                    action = self.queue.get(True, 0.1)
                    action.act(self.device, self.current_state)
            except Queue.Empty as e:
                continue

        self.device.disconnect()

    def join(self, timeout=None):
        self.alive.clear()
        threading.Thread.join(self, timeout)
