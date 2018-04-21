############################################
#        4,6,2017     10:31 AM             #
#               by resbi                   #
#   version 1.0.1.0    4,6,2017 11:11 AM   #
#   Last change time:  4/15/2018 13:19     #
#   1.0.1.0:   Change pinnumber's caculate #
############################################
import os,time

"""
pins = 

for k in range(26):
    for m in range(50):
        a = "P{}{}".format(chr(65 + k), m)
        pinnum = (k * 32) + m
        pins[a] = pinnum
"""
                        
def scanpin(pin):
#if not(pin in list(pins.keys())):
    i = ord(pin[1].upper()) - 65
    #if i > 11:
    #    print("No this GPIO!")
    #    end(1,pin)
    pinnum = (i * 32) + int(pin[2:])
#    else:
#    pinnum = pins[pin]
#    print(pinnum)
    return(pinnum)

def end(error, pin):
    if error == 1:
        print("error:No this gpio %s" % (pin))
    if error == 2:
        print("error:No this mode")
    if error == 3:
        print("You must mount the pin behind you do it!")
    exit()

def SetValue(pin, value):
    pinnum = scanpin(pin)
    f = open("/sys/class/gpio/gpio{}/value".format(pinnum), "at")
    f.write(str(value))
    f.close()
    
def pinMount(pin):
    os.system("echo {} >> /sys/class/gpio/export".format(scanpin(pin)))
    #f = open("/sys/class/gpio/export", "at")
    #f.write(str(scanpin(pin)))
    #f.close()

def pinUmount(pin):
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    #os.system("echo {} >> /sys/class/gpio/unexport".format(scanpin(pin)))
    f = open("/sys/class/gpio/unexport", "at")
    f.write(str(scanpin(pin)))
    f.close()
    
def pinMode(pin, mode, isprint = "no"):
    if mode != "out":
        if mode != "in":
            end(2, pin)
    if isprint == "on":
        print("The pin %s in set mode to %s ." % (pin, mode))
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    pinnum = scanpin(pin)
    #os.system("echo {} >> /sys/class/gpio/gpio{}/direction".format(mode, pinnum))
    f = open("/sys/class/gpio/gpio{}/direction".format(pinnum), "at")
    f.write(str(mode))
    f.close()

def pinValue(pin, value, isprint = "no"):
    if value == "high":
        value = 1
    if value == "low":
        value = 0
    if isprint == "on":
        print("The pin %s is set value on %s ." % (pin, value))
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    #os.system("echo "+str(value)+" > /sys/class/gpio/gpio"+str(pinnum)+"/value")
    SetValue(pin, value)
    
def pinPwm(pin, hz, tm, isprint = "no"):
    pinnum = scanpin(pin)
    if isprint == "on":
        print("The pin %s is in %s hz,with %s ." % (pin, hz, tm))
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum)) == "False":end(3,pin)
    if tm == "long":
        while 1:
            time.sleep(1 / hz / 2)
            SetValue(pin, 1)

            time.sleep(1 / hz / 2)
            SetValue(pin, 0)

    time_temp = time.time()
    while time.time() - time_temp < tm:
        time.sleep(1 / hz)
        SetValue(pin, 1)

        time.sleep(1 / hz)
        SetValue(pin, 0)


