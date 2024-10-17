# #!/bin/env python

# from matplotlib import pyplot as plt
# import csv

# import multiprocessing
# device_manager = DeviceManager()

# selDevice = None
# for device in device_manager.devices:
#     if "Razer" in device.name:
#         selDevice = device
#         print("test: ",dir(selDevice))

# if None == selDevice:
#     print("n/a")
#     exit

# print(selDevice.battery_level)

# logFile = open("razerBatteryLog.csv", "w+").close()


# values = []

# class BatteryLog:
#     def __init__(self, selDevice):
#         device = selDevice
#         self.time = dt.now()
#         self.level = device.battery_level
#         self.log = "razerBatteryLog.csv"
#         self.sleep = 1
        
#     def __str__(self):
#         return f"{self.time},{self.level}"
    
#     def main(self):
#         # threaded
#         multiprocessing.Process(target=self.update).start()
#         multiprocessing.Process(target=self.plot).start()
        
    
#     def update(self):
#         while True:
#             self.time = dt.now()
#             with open(self.log, "a+") as logFile:
#                 logFile.write(str(self))
#                 logFile.write("\n")
#             values.append([self.time,self.level])
#             print(self.level)
#             sleep(self.sleep)
            
        
#     def plot(self):
        
#         while True:
#             plt.plot(values)
#             plt.show()
#             sleep(self.sleep)
        
# BatteryLog(selDevice).main()


import matplotlib.pyplot as plt
import matplotlib
import random
from time import sleep
from datetime import datetime as dt
from openrazer.client import DeviceManager
import csv
plt.ion()  # turning interactive mode on
matplotlib.use("Qt5agg") # or "Qt5agg" depending on you version of Qt

class valuesClass:
    def __init__(self):
        self.x = []
        self.y = []
        
values = valuesClass()

device_manager = DeviceManager()

selDevice = None
for device in device_manager.devices:
    if "Razer" in device.name:
        selDevice = device
        print("test: ",dir(selDevice))

if None == selDevice:
    print("Device not found")
    exit
    
def mypause(interval):
    manager = plt._pylab_helpers.Gcf.get_active()
    if manager is not None:
        canvas = manager.canvas
        if canvas.figure.stale:
            canvas.draw_idle()        
        #plt.show(block=False)
        canvas.start_event_loop(interval)
    else:
        sleep(interval)


plt.show(block=False)

with open('razerBattery.csv','r') as file:
    x = csv.reader(file)
    for row in x:
        values.x.append(dt.strptime(row[0],'%Y-%m-%d %H:%M:%S.%f'))
        values.y.append(int(row[1]))


values.x.append(dt.now())
values.y.append(selDevice.battery_level)
# plotting the first frame
graph = plt.plot(values.x,values.y)
plt.ylim(0,10)
plt.pause(1)
 
# set range of y-axis 0-100
plt.ylim(0,100)
 
# the update loop
while(True):
    # updating the data
    values.x.append(dt.now())
    values.y.append(selDevice.battery_level)
    
    # writing the newer data to the file
    with open('razerBattery.csv','a+') as file:
        x = csv.writer(file)
        x.writerow([values.x[-1],values.y[-1]])

    # plotting newer graph
    graph = plt.plot(values.x,values.y,color = 'g')[0]
     
    # calling pause function for 0.25 seconds
    mypause(120)
