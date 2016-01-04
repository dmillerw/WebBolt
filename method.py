import gatt
import state

state_map = {}

def get_state(address):
    if state_map.get(address) is None or state_map.get(address) is False:
        device = gatt.connect(address)
        state_map[address] = state.from_device(device)
        return state_map[address]
    else:
        return state_map[address]

def toggle(address):
    current_state = get_state(address)
    device = gatt.connect(address)
    new_state = state.from_device(device)

    if str(current_state.get_brightness()) != '0':
        if str(new_state.get_brightness()) == '0':
            new_state.set_brightness(current_state.get_brightness())
        else:
            new_state.set_brightness(0)
    else:
        state_map[address].set_brightness(100)
        new_state.set_brightness(100)

    new_state.write(device)

    device.disconnect()

def set_scene(address, scene):
    if scene == 'bright':
        device = gatt.connect(address)
        s = state.from_rgb(255, 255, 255, 100)
        state_map[address] = s
        s.write(device)
    elif scene == 'night':
        device = gatt.connect(address)
        s = state.from_rgb(48, 24, 96, 25)
        state_map[address] = s
        s.write(device)

def set_color(address, red, green, blue):
    s = get_state(address)
    device = gatt.connect(address)
    s.set_rgb(red, green, blue)
    state_map[address] = s
    s.write(device)

def set_temperature(address, temperature):
    s = get_state(address)
    device = gatt.connect(address)
    s.set_temperature(temperature)
    state_map[address] = s
    s.write(device)

def set_brightness(address, brightness):
    s = get_state(address)
    device = gatt.connect(address)
    s.set_brightness(brightness)
    state_map[address] = s
    s.write(device)
