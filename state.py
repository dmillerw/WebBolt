MAX_LENGTH = 36

def from_device(device):
    return from_hex_stream(device.read('0012').replace(' ', '').decode('hex'))

def from_hex_stream(stream):
    if len(stream.replace(chr(00), '')) == 0:
        s = state()
        s.set_rgb(255, 255, 255)
        s.set_brightness(100)
        return s

    if stream[:5] == 'CLTMP':
        data = stream[6:]
        first = data.find(',')
        temp = data[:first]
        second = data.find(',', first + 1)
        brightness = data[first + 1:second]

        s = state()
        s.set_temperature(temp)
        s.set_brightness(brightness)
        return s
    else:
        data = stream.split(',')

        s = state()
        s.set_rgb(data[0], data[1], data[2])
        s.set_brightness(data[3])
        return s

def from_rgb(red, green, blue, brightness):
    s = state()
    s.set_rgb(red, green, blue)
    s.set_brightness(brightness)
    return s

class state():

    def __init__(self):
        self.type = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.brightness = 0
        self.temperature = 0

        self.old_type = 0
        self.old_red = 0
        self.old_green = 0
        self.old_blue = 0
        self.old_brightness = 0
        self.old_temperature = 0

    def store_previous(self):
        self.old_type = self.type
        self.old_red = self.red
        self.old_green = self.green
        self.old_blue = self.blue
        self.old_brightness = self.brightness
        self.old_temperature = self.temperature

    def revert_to_previous(self):
        self.type = self.old_type
        self.red = self.old_red
        self.green = self.old_green
        self.blue = self.old_blue
        self.brightness = self.old_brightness
        self.temperature = self.old_temperature

    def get_type(self):
        return self.type

    def get_rgb(self):
        if self.get_type() == 0:
            return self.red, self.green, self.blue
        else:
            return 0, 0, 0

    def get_brightness(self):
        return self.brightness

    def set_rgb(self, red, green, blue):
        self.store_previous()

        self.type = 0
        self.red = red
        self.green = green
        self.blue = blue

    def set_temperature(self, temperature):
        self.store_previous()

        self.type = 1
        self.temperature = temperature

    def set_brightness(self, brightness):
        self.store_previous()

        self.brightness = brightness

    def __str__(self):
        if self.get_type() == 0:
            return '{type: RGB, red: ' + str(self.red)+ ', green: ' + str(self.green) + ', blue: ' + str(self.blue) + ', brightness: ' + str(self.brightness) + '}'
        else:
            if self.get_type() == 1:
                return '{type: TEMP, temperature: ' + self.temperature + ', brightness: ' + self.brightness + '}'
            else:
                return 'ERROR'

    def write_rgb(self, device):
        red = str(self.red)
        green = str(self.green)
        blue = str(self.blue)
        brightness = str(self.brightness)

        red = ''.join(hex(ord(x))[2:] for x in red)
        green = ''.join(hex(ord(x))[2:] for x in green)
        blue = ''.join(hex(ord(x))[2:] for x in blue)
        brightness = ''.join(hex(ord(x))[2:] for x in brightness)

        stream = red + '2c' + green + '2c' + blue + '2c' + brightness
        for i in range((MAX_LENGTH - len(stream)) / 2):
            stream = stream + '2c'

        device.write('0012', stream)

    def write_temperature(self, device):
        temperature = str(self.temperature)
        brightness = str(self.brightness)

        temperature = ''.join(hex(ord(x))[2:] for x in temperature)
        brightness = ''.join(hex(ord(x))[2:] for x in brightness)

        stream = '434c544d5020' + temperature + '2c' + brightness
        for i in range((MAX_LENGTH - len(stream)) / 2):
            stream = stream + '2c'

        device.write('0012', stream)

    def write(self, device):
        if self.get_type() == 0:
            self.write_rgb(device)
        else:
            if self.get_type() == 1:
                self.write_temperature(device)
