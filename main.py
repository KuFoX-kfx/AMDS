#Import 
from PyQt5 import QtWidgets, QtGui
import Discord_API
import tray
import UI_API
from API import D_API
import json
import threading
import sys
import time


#Import tray class
def start_animate():
    tray.SystemTrayIcon.startbtn()
    tray.SystemTrayIcon.stopbtn()
    
def stop_animate():
    for i in threading.enumerate():
        if i.name=="sss":
            tray.SystemTrayIcon.start.setEnabled(True)
            tray.SystemTrayIcon.stop.setEnabled(False)






def AnimateStatus(self):
        with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
        DAPI = Discord_API.Discord_API(data["authToken"])
        while(self.event):
            for i in range(len(data["animation"])):
                DAPI.set_cstatus(text=data["animation"][i]["text"], emoji=data["animation"][i]["emoji_name"])
                time.sleep(data["timeout"]/1000)
    


#with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
#with open("AMDS-kfx.json", "w") as json_file: json.dump(data, json_file)



t1 = threading.Thread(target=lambda: tray.start())
t1.start()
def test():
    while(True): 
        print(tray.getanimate())
        time.sleep(1)
t2 = threading.Thread(target=test)
t2.start()

tray.SystemTrayIcon.

t1.join()


    
    
#app = QtWidgets.QApplication(sys.argv)
#w = QtWidgets.QWidget()
#tray_icon = tray.SystemTrayIcon(QtGui.QIcon("icon.png"), w)
#tray_icon.show()
#tray_icon.showMessage('Animate my discord status', 'Start the AMDS')
#tray_icon.start.triggered.connect(start_animate)
#tray_icon.stop.triggered.connect(stop_animate)
#
#event = True
#sas = threading.Thread(target=start_as)
#sas.setName("sss")
#
#tray_icon.start.setEnabled(True)
#tray_icon.stop.setEnabled(False)
#


#sys.exit(app.exec_())