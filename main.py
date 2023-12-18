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
event = threading.Event()


#Import tray class
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Animate my discord status')
        self.menu = QtWidgets.QMenu(parent)
        self.menu.addAction("AMDS By KuFoX").setEnabled(False)
        
        self.menu.addSeparator()

        self.settings = self.menu.addAction("Open Settings")
        #settings.triggered.connect()
        self.settings.setIcon(QtGui.QIcon("icon.png"))

        self.start = self.menu.addAction("Start")
        self.start.triggered.connect(start_animate)
        self.start.setIcon(QtGui.QIcon("icon.png"))
        
        self.stop = self.menu.addAction("Stop")
        self.stop.triggered.connect(stop_animate)
        self.stop.setIcon(QtGui.QIcon("icon.png"))

        self.menu.addSeparator()
        self.setContextMenu(self.menu)
        #self.activated.connect(self.onTrayIconActivated)
        
    def set_start(self):
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
    def set_stop(self):
        self.start.setEnabled(False)
        self.stop.setEnabled(True)

def start_tray():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('Animate my discord status', 'Start the AMDS')
    SystemTrayIcon.set_stop(SystemTrayIcon)
    sys.exit(app.exec_())
    


def start_animate():
    sas = threading.Thread(target=start_as)
    sas.setName("sss")
    sas.start()
    SystemTrayIcon.set_start
    
def stop_animate():
    for i in threading.enumerate():
        if i.name=="sss":
            event.set()
            SystemTrayIcon.set_stop


def start_as():
    with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
    DAPI = Discord_API.Discord_API(data["authToken"])
    while(True):
        if event.is_set():
            break
        for i in range(len(data["animation"])):
            DAPI.set_cstatus(text=data["animation"][i]["text"], emoji=data["animation"][i]["emoji_name"])
            time.sleep(data["timeout"]/1000)
    


#with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
#with open("AMDS-kfx.json", "w") as json_file: json.dump(data, json_file)

    
def start():
    threading.Thread(target=start_tray).start()
    #startAS = threading.Thread(target=start_as).start()

    




start()