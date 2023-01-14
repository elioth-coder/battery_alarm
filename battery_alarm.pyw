import threading
from tkinter.messagebox import *
from Battery import Battery

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def monitorBattery():
    battery = Battery()
    
    if(battery.critical()):
        return showderror("Your battery's in critical level! [" + str(battery.percentage()) + "%]")

    if(battery.needsCharging()):
        return showwarning("Your battery needs charging! [" + str(battery.percentage()) + "%]")
    
    if(battery.enoughCharging()()):
        return showinfo("Your battery's almost full! [" + str(battery.percentage()) + "%]")

setInterval(monitorBattery,1)