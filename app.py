import web
import action
import utils

urls = (
    '/device/(.*)/state', 'GetState',
    '/device/(.*)/toggle', 'Toggle',
    '/device/(.*)/scene/(.*)', 'SetScene',
    '/device/(.*)/color/set', 'SetColor',
    '/device/(.*)/brightness/set', 'SetBrightness'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

# Route classes

class GetState:
    def GET(self, address):
        s = action.thread.current_state
        val = ''

        if s.get_type() == 0:
            r, g, b = s.get_rgb()
            val = 'RED: ' + str(r) + '\nGREEN: ' + str(g) + '\nBLUE: ' + str(b) + '\nBRIGHTNESS: ' + str(s.get_brightness())
        else:
            val = 'TEMPERATURE: ' + str(s.get_temperature()) + '\nBRIGHTNESS: ' + str(s.get_brightness())

        return val

class Toggle:
    def GET(self, address):
        action.thread.queue.put(action.ActionToggle())
        return 'OK'

class SetScene:
    def GET(self, address, scene):
        action.thread.queue.put(action.ActionScene(scene))
        return 'OK'

class SetColor:
    def GET(self, address):
        i = web.input()
        r = utils.try_get_input(i, 'red', 0)
        g = utils.try_get_input(i, 'green', 0)
        b = utils.try_get_input(i, 'blue', 0)
        action.thread.queue.put(action.ActionSetRGB(r, g, b))

class SetBrightness:
    def GET(self, address):
        i = web.input()
        b = utils.try_get_input(i, 'brightness', 0)
        action.thread.queue.put(action.ActionSetBrightness(b))
