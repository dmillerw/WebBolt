import base_action
import time

class ActionSleep(base_action.Action):

    def act(self, device, current_state):
        time.sleep(1)
