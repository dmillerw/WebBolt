import gatt

def p(device, handle):
    val = device.read(handle)
    print(handle)
    print(val)
    print(val.replace(' ', '').decode('hex'))

device = gatt.connect('20:C3:8F:F3:09:98')
p(device, '0015')
p(device, '0018')
# p(device, '001b')
p(device, '001f')
# p(device, '0022')
p(device, '0026')
# p(device, '0029')
p(device, '002c')
p(device, '0030')
device.disconnect()
