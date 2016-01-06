import web
import action

urls = (
    '/device/(.*)/state', 'GetState',
    '/device/(.*)/toggle', 'Toggle',
    '/device/(.*)/scene/(.*)', 'SetScene'
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
