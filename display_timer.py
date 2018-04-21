import display
import gpio
import time

#pin = "PD5"
#gpio.pinMount(pin)
#gpio.pinMode(pin, "out", "on")

#hz = 4000
#tm = 0.01

def divideToSet(content, howlong):
    result = []
    for k in range(howlong, len(content) + 1, howlong):
        d = content[k-howlong : k]
        a = [int(m) for m in d]
        result += [a]
    return result

#for k in range(2**32):
while 1:
    k = int(time.time())
    sets = bin(k).replace("0b", "").zfill(32)
    sets = divideToSet(sets, 4)
#    print(sets)
    stime = time.time()
#    gpio.pinPwm(pin, hz, tm, "on")
    while time.time() - stime < 1:
        display.display(sets)
