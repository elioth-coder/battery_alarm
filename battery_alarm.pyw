import threading
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
        message = "Your battery's in critical level! Battery level " + str(battery.percentage()) + "%! Please charge!"
        tts.speak(message)

        return

    if(battery.needsCharging()):
        message = "Your battery needs charging! Battery level " + str(battery.percentage()) + "%! Please charge!"
        tts.speak(message)

        return
    
    if(battery.enoughCharging()):
        message = "Your battery's almost full! Battery level " + str(battery.percentage()) + "%! Please plug out!"
        tts.speak(message)

        return
        
setInterval(monitorBattery,1)