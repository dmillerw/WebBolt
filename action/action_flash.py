import base_action
import time

class ActionFlash(base_action.Action):

    def __init__(self, flash, duration):
        self.flash = flash
        self.duration = duration

    def act(self, device, current_state):
        self.flash.write(device)
        time.sleep(float(self.duration))
        current_state.write(device)
