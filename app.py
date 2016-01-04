import utils
import web
import method
import threads
import state

urls = (
    '/device/(.*)/state', 'GetState',
    '/device/(.*)/toggle', 'Toggle',
    '/device/(.*)/scene/(.*)', 'SetScene',
    '/device/(.*)/color/set', 'SetColor',
    '/device/(.*)/temperature/set', 'SetTemperature',
    '/device/(.*)/brightness/set', 'SetBrightness',
    '/device/(.*)/flash', 'Flash'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

# Route classes

class GetState:
    def GET(self, address):
        s = method.get_state(address)
        val = ''

        if s.get_type() == 0:
            r, g, b = s.get_rgb()
            val = 'RED: ' + str(r) + '\nGREEN: ' + str(g) + '\nBLUE: ' + str(b) + '\nBRIGHTNESS: ' + str(s.get_brightness())
        else:
            val = 'TEMPERATURE: ' + str(s.get_temperature()) + '\nBRIGHTNESS: ' + str(s.get_brightness())

        return val

class Toggle:
    def GET(self, address):
        method.toggle(address)
        return 'OK'

class SetScene:
    def GET(self, address, scene):
        method.set_scene(address, scene)
        return 'OK'

class SetColor:
    def GET(self, address):
        input = web.input()
        red = utils.try_get_input(input, 'red', 0)
        green = utils.try_get_input(input, 'green', 0)
        blue = utils.try_get_input(input, 'green', 0)
        method.set_color(address, red, green, blue)
        return 'OK'

class SetTemperature:
    def GET(self, address):
        temperature = utils.try_get_input(web.input(), 'temperature', 0)
        method.set_temperature(address, temperature)
        return 'OK'

class SetBrightness:
    def GET(self, address):
        brightness = utils.try_get_input(web.input(), 'brightness', 0)
        method.set_brightness(address, brightness)
        return 'OK'

class Flash:
    def GET(self, address):
        input = web.input()
        red = utils.try_get_input(input, 'red', 0)
        green = utils.try_get_input(input, 'green', 0)
        blue = utils.try_get_input(input, 'blue', 0)
        duration = utils.try_get_input(input, 'duration', 5)

        s = method.get_state(address)
        t = threads.FlashThread(address, s, state.from_rgb(red, green, blue, s.get_brightness()), duration)
        t.start()

        return 'OK'
