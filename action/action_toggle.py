import action

class ActionToggle(action.Action):

    def act(self, device, current_state):
        if int(current_state.get_brightness()) == 0:
            current_state.set_brightness(current_state.old_brightness)
        else:
            current_state.set_brightness(0)

        current_state.write(device)
