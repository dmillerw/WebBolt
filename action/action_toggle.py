import base_action

class ActionToggle(base_action.Action):

    def act(self, device, current_state):
        if int(current_state.get_brightness()) == 0:
            current_state.set_brightness(100)
        else:
            current_state.set_brightness(0)

        current_state.write(device)
