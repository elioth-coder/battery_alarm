from tkinter import *
from tkinter import font
import psutil
import threading
import winsound

root = Tk()
root.title("Battery Status")
root.wm_attributes("-topmost", 1)
root.wm_attributes("-toolwindow", 1)
root.geometry("210x25+500+0")

fontStyle = font.Font(family="Lucida Grande", size=16)
label = Label(root, text="Loading...", anchor='w', font=fontStyle)
label.pack(fill='both')

def isPluggedIn():
  battery = psutil.sensors_battery()
  return battery.power_plugged

def getBatteryStatus(): 
  battery = psutil.sensors_battery()
  status  = " PLUGGED IN" if (isPluggedIn()) else " ON BATTERY"
  status += " - " + str(battery.percent) + "%"
  return status

def needsCharging(): 
  battery = psutil.sensors_battery()
  return (not isPluggedIn() and battery.percent <= 20)

def forPlugOut():
  battery = psutil.sensors_battery()
  return (isPluggedIn() and battery.percent >= 80)
 
def isBatteryLevelCritical(): 
  battery = psutil.sensors_battery()
  return (not isPluggedIn() and battery.percent <= 10)

def isWindowVisible(): 
  return root.state() == 'normal'

def show(): 
  if not isWindowVisible():
    root.deiconify()

def hide(): 
  if isWindowVisible():
    root.withdraw()

def beep(times):
  for x in range(times-1):
    winsound.Beep(440, 1000)

def repeat(): 
  label['text'] = getBatteryStatus()
  if isBatteryLevelCritical(): 
    # os.system("shutdown /s /t 1")
    beep(10)

  if(needsCharging() or forPlugOut()): 
    show()
    beep(10)
  else: 
    hide()
  threading.Timer(15.0, repeat).start()

repeat()
root.mainloop()