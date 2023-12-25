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
    #Fill all
    try:
        with open("AMDS-kfx.config.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
    except: 
        data = {
                 "timer": 15,
                 "authToken": "",
                 "status": "Online",
                 "animation": [{"text": "AMDS By KuFoX", "emoji_name": "\u2139\ufe0f"}]
                 }   
        with open("AMDS-kfx.config.json", "w+", encoding="utf8") as json_file:        
            json.dump(data, json_file) 
        
    UI.ui.TBLW_main.setRowCount(len(data["animation"]))

    UI.ui.SPNBOX_Time.setValue(int(data["timer"]))
    
    if(data["status"]=="Online"): UI.ui.CMBBOX_Status.setCurrentIndex(0)
    elif(data["status"]=="Idle"): UI.ui.CMBBOX_Status.setCurrentIndex(1)
    elif(data["status"]=="DND"): UI.ui.CMBBOX_Status.setCurrentIndex(2)
    elif(data["status"]=="Invisible"): UI.ui.CMBBOX_Status.setCurrentIndex(3)
    
    UI.ui.PRGRSBAR_CurrentStep.setValue(0)
    UI.ui.PRGRSBAR_CurrentStep.setMaximum(len(data["animation"]))
    
    UI.ui.LNEDIT_APIToken.setText(data["authToken"])
    
    for i in range(len(data["animation"])):
        UI.ui.TBLW_main.setItem(i, 0, QtWidgets.QTableWidgetItem(data["animation"][i]["text"]))
        UI.ui.TBLW_main.setItem(i, 1, QtWidgets.QTableWidgetItem(data["animation"][i]["emoji_name"]))
        

def SHAPI():
    print(UI.ui.CHKBOX_APIToken.isChecked())
    if(UI.ui.CHKBOX_APIToken.isChecked()==True):
        UI.ui.LNEDIT_APIToken.setEchoMode(QtWidgets.QLineEdit.EchoMode(0))
    elif(UI.ui.CHKBOX_APIToken.isChecked()==False):
        UI.ui.LNEDIT_APIToken.setEchoMode(QtWidgets.QLineEdit.EchoMode(2))
        
        
def savejson():
    data = {
             "timer": 15,
             "authToken": "",
             "status": "",
             "animation": []
            }
    data["timer"] = UI.ui.SPNBOX_Time.value()
    data["authToken"] = UI.ui.LNEDIT_APIToken.text()
    data["status"] = UI.ui.CMBBOX_Status.currentText()
    for i in range(UI.ui.TBLW_main.rowCount()):
        
        try: text = UI.ui.TBLW_main.item(i, 0).text()
        except: text = None
        
        try: emoji = UI.ui.TBLW_main.item(i, 1).text()
        except: emoji = None
        
        try: status = UI.ui.TBLW_main.item(i, 2).text()
        except: status = None
        
        try: timer = UI.ui.TBLW_main.item(i, 3).text()
        except: timer = None
        
        data["animation"].append({"text": text, "emoji_name": emoji, "status": status, "timer": timer})
    with open("AMDS-kfx.config.json", "w+") as json_file: json.dump(data, json_file)
        
    

    

    
    
    
    
    
    
    
    
    
    
    

    
#thr_gui = threading.Thread(target=UI.show())





def startmain():
    UI.ui.PSHBTN_Update.clicked.connect(update_ui)
    UI.ui.PSHBTN_Save.clicked.connect(savejson)
    UI.ui.CHKBOX_APIToken.stateChanged.connect(SHAPI)
    
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