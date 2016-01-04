import gatt
import state
import threading
import time

class FlashThread(threading.Thread):
    def __init__(self, address, current_state, temp_state, duration):
        super(FlashThread, self).__init__()
        self.address = address
        self.current_state = current_state
        self.temp_state = temp_state
        self.duration = duration

    def run(self):
        device = gatt.connect(self.address)
        self.temp_state.write(device)
        time.sleep(float(self.duration))
        self.current_state.write(device)
        device.disconnect()
