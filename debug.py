import gatt
import state
import time
import random

device = gatt.connect('20:C3:8F:F3:09:98')
s = state.from_rgb(0, 0, 0, 5)

while True:
    s.set_rgb(random.randrange(25, 100), random.randrange(25, 100), random.randrange(25, 100))
    s.write(device)
