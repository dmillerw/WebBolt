import base_action

class ActionSetBrightness(base_action.Action):

    def __init__(self, b):
        self.b = b

    def act(self, device, current_state):
        current_state.set_brightness(self.b)
        current_state.write(device)
