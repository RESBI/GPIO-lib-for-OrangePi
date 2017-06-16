############################################
#        4,6,2017     10:31 AM             #
#               by resbi                   #
#    thanks: the creator of lib:os,time    #
#   version 1.0.0.1    16.6,2017 13:00     #
############################################
import os,time

def scanpin(pin):
    i = 0
    a = ["A","B","C","D","E","F","G","H","I","J","K","L"]
    while pin[1] != a[i]:
        i += 1
        if i > 11:
            print("No this GPIO!")
            i = 0
            end(1,pin)
    pinnum = (i * 32) + int(pin[2])
    return(pinnum)

def end(error,pin):
    if error == 1:
        print("error:No this gpio %s" % (pin))
    if error == 2:
        print("error:No this mode")
    if error == 3:
        print("You must mount the pin behind you do it!")
    exit()

def pinMount(pin):
    os.system("echo "+str(scanpin(pin))+" >> /sys/class/gpio/export")

def pinUmount(pin):
    pinnum = scanpin(pin)
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    os.system("echo "+str(pinnum)+" >> /sys/class/gpio/unexport")

def pinMode(pin,mode,isprint):
    if mode != "out":
        if mode != "input":
            end(2,pin)
    pinnum = scanpin(pin)
    if isprint == "on":
        print("The pin %s in set mode to %s ." % (pin,mode))
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    os.system("echo "+mode+" >> /sys/class/gpio/gpio"+str(pinnum)+"/direction")

def pinValue(pin,value,isprint):
    if value == "high":
        value = 1
    if value == "low":
        value = 0
    if isprint == "on":
        print("The pin %s is set value on %s ." % (pin,value))
    pinnum = scanpin(pin)
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum) == "False":end(3,pin)
    os.system("echo "+str(value)+" > /sys/class/gpio/gpio"+str(pinnum)+"/value")

def pinPwm(pin,hz,tm,isprint):
    pinnum = scanpin(pin)
    if isprint == "on":
        print("The pin %s is in %s hz,with %s ." % (pin,hz,tm))
    #if os.path.exists("/sys/class/gpio/gpio"+str(pinnum)) == "False":end(3,pin)
    if tm == "long":
        while 1:
            time.sleep((float(1) / float(hz)) / 2)
            os.system("echo 1  > /sys/class/gpio/gpio"+str(pinnum)+"/value")
            time.sleep((float(1) / float(hz)) / 2)
            os.system("echo 0  > /sys/class/gpio/gpio"+str(pinnum)+"/value")
    time_temp = time.time()
    while time.time() - time_temp < float(tm):
        time.sleep(float(1) / float(hz))
        os.system("echo 1  > /sys/class/gpio/gpio"+str(pinnum)+"/value")
        time.sleep(float(1) / float(hz))
        os.system("echo 0  > /sys/class/gpio/gpio"+str(pinnum)+"/value")
