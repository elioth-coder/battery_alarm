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
        return showerror(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            "Your battery's in critical level!"
        )

    if(battery.needsCharging()):
        return showwarning(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            "Your battery needs charging!"
        )
    
    if(battery.enoughCharging()):
        return showinfo(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            "Your battery's almost full!"
        )
        
setInterval(monitorBattery,1)