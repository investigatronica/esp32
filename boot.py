import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('No es Ulan Bator', 'noesedupublica!')
    while not wlan.isconnected():
        pass
