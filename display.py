import gpio
import time


xpins = ["PH3", "PD1", "PD0", "PD6"]
ypins = ["PC4", "PD2", "PD3", "PB4", "PB5", "PB2", "PB6", "PB7"]#, "PD5"]

pins = xpins + ypins

for pin in pins:
    gpio.pinMount(pin)
    gpio.pinMode(pin, "out")

def pOut(digits):
    for i in range(len(digits)):
        gpio.pinValue(xpins[i], digits[i])

#print(gpio.pins)
a = 0
for k in range(2):
    a = a^1
    pOut([a for i in range(4)])
#    time.sleep(1)

def display(sets):
#    starttime = time.time()
    for k in range(len(sets)):
#        nowa = time.time() - starttime
#        nowa = int(nowa * 810) % len(sets)
        pOut(sets[k])
        gpio.pinValue(ypins[k], 1)
#        time.sleep(0.001)
        gpio.pinValue(ypins[k], 0)

x = [
[1, 0, 1, 0],
[0, 1, 0, 1],
[1, 0, 1, 0],
[0, 1, 0, 1]
]
#while 1:
#    display(x)
