import base_action
import random

class ActionScene(base_action.Action):

    def __init__(self, scene):
        self.scene = scene

    def act(self, device, current_state):
        if self.scene == 'bright':
            current_state.set_rgb(255, 255, 255)
            current_state.set_brightness(100)
        elif self.scene == 'night':
            current_state.set_rgb(48, 24, 96)
            current_state.set_brightness(25)
        elif self.scene == 'random':
            current_state.set_rgb(random.randrange(255), random.randrange(255), random.randrange(255))
            current_state.set_brightness(100)

        current_state.write(device)
