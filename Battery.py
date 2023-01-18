import psutil

class Battery:
    def __init__(self):
        self.sensor = psutil.sensors_battery()

    def percentage(self):
        return self.sensor.percent

    def pluggedIn(self):
        return self.sensor.power_plugged

    def needsCharging(self): 
        return (not self.pluggedIn() and self.percentage() <= 20)

    def enoughCharging(self):
        return (self.pluggedIn() and self.percentage() >= 80)
    
    def critical(self): 
        return (not self.pluggedIn() and self.percentage() <= 10)
