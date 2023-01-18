import threading
from tkinter.messagebox import *
from Battery import Battery
from TextToSpeech import TextToSpeech

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def monitorBattery():
    battery = Battery()
    tts = TextToSpeech()
    
    if(battery.critical()):
        message = "Your battery's in critical level!"
        tts.speak(message)

        return showerror(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            message
        )

    if(battery.needsCharging()):
        message = "Your battery needs charging!"
        tts.speak(message)

        return showwarning(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            message
        )
    
    if(battery.enoughCharging()):
        message = "Your battery's almost full!" 
        tts.speak(message)

        return showinfo(
            "Battery Level - [" + str(battery.percentage()) + "%]",
            message
        )
        
setInterval(monitorBattery,1)