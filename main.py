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

UI = UI_API.UI_API()




def start_animate():
    pass
    #tray.SystemTrayIcon.startbtn()
    #tray.SystemTrayIcon.stopbtn()
    
def stop_animate():
    for i in threading.enumerate():
        if i.name=="sss":
            pass
            #tray.SystemTrayIcon.start.setEnabled(True)
            #tray.SystemTrayIcon.stop.setEnabled(False)

def AnimateStatus():
        with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
        DAPI = Discord_API.Discord_API(data["authToken"])
        while(event):
            for i in range(len(data["animation"])):
                DAPI.set_cstatus(text=data["animation"][i]["text"], emoji=data["animation"][i]["emoji_name"])
                time.sleep(data["timeout"]/1000)
    
    
def update_ui():
    print("Update")
    #Fill all
    with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
    
    UI.ui.TBLW_main.setRowCount(len(data["animation"]))
    
    UI.ui.SPNBOX_Time.setValue(int(data["timeout"]/1000))
    
    if(data["status"]=="online"): UI.ui.CMBBOX_Status.setCurrentIndex(0)
    elif(data["status"]=="idle"): UI.ui.CMBBOX_Status.setCurrentIndex(1)
    elif(data["status"]=="dnd"): UI.ui.CMBBOX_Status.setCurrentIndex(2)
    elif(data["status"]=="invisible"): UI.ui.CMBBOX_Status.setCurrentIndex(3)
    
    UI.ui.PRGRSBAR_CurrentStep.setValue(0)
    UI.ui.PRGRSBAR_CurrentStep.setMaximum(len(data["animation"]))
    
    for i in range(len(data["animation"])):
        UI.ui.TBLW_main.setItem(i, 0, QtWidgets.QTableWidgetItem(data["animation"][i]["text"]))
        UI.ui.TBLW_main.setItem(i, 1, QtWidgets.QTableWidgetItem(data["animation"][i]["emoji_name"]))
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    

    
#thr_gui = threading.Thread(target=UI.show())





def startmain():
    UI.ui.PSHBTN_Update.clicked.connect(update_ui)
    
    
    thr_animatestatus = threading.Thread(target=AnimateStatus, name="animatestatus")

    update_ui()
    UI.show()
    

startmain()
#with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
#with open("AMDS-kfx.json", "w") as json_file: json.dump(data, json_file)

#t1 = threading.Thread(target=lambda: tray.start())
#t1.start()
#
##threading.Thread(target=lambda: print(tray.SystemTrayIcon.getanimate())).start()
#def test():
#    while(True): 
#        print(tray.getanimate())
#        time.sleep(1)
#t2 = threading.Thread(target=test)
#t2.start()
#
#
#t1.join()

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