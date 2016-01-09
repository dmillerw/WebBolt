import base_action

class ActionSetRGB(base_action.Action):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def act(self, device, current_state):
        current_state.set_rgb(self.r, self.g, self.b)
        current_state.write(device)
