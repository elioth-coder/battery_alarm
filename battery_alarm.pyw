from tkinter import *
from tkinter import font
import psutil
import threading
import winsound
from pystray import MenuItem as item
import pystray
from PIL import Image

root = Tk()
root.title("Battery Status")
root.wm_attributes("-topmost", 1)
root.wm_attributes("-toolwindow", 1)
screen_height = root.winfo_screenheight()
matrix = "210x25+0+" + str(screen_height - 115)
root.geometry(matrix)

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

def beep(times):
  for x in range(times-1):
    winsound.Beep(440, 1000)

def quit_window(icon, item):
   icon.stop()
   root.destroy()

def showWindow(icon, item):
   icon.stop()
   root.after(0,root.deiconify())

def hideWindow():
   root.withdraw()
   image=Image.open("favicon.ico")
   menu=(item('Quit', quit_window), item('Show', showWindow))
   icon=pystray.Icon("battery", image, "Battery Alarm", menu)
   icon.run()

root.protocol('WM_DELETE_WINDOW', hideWindow)

def repeat(): 
  label['text'] = getBatteryStatus()
  if isBatteryLevelCritical(): 
    beep(10)

  if(needsCharging() or forPlugOut()): 
    showWindow()
    beep(10)

  threading.Timer(15.0, repeat).start()

repeat()
root.mainloop()