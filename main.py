#Import 
from PyQt5 import QtWidgets, QtGui
import Discord_API
import tray
import UI_API
from API import D_API
import json
import threading
import sys
import urllib.request 
import os
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
    
    
def update_profile():
    #Fill all
    try:
        with open(f"Profiles\{UI.ui.CMBBOX_SelectProfile.currentText()}.AMDS-prfl.kfx", "r", encoding="utf8") as json_file: data = json.load(json_file)
        print("load")
    except: 
        with open("Profiles\Default.AMDS-prfl.kfx", "r", encoding="utf8") as json_file: data = json.load(json_file)
        print("default load")
        
    UI.ui.TBLW_main.setRowCount(len(data["animation"]))

    UI.ui.SPNBOX_Time.setValue(int(data["timer"]))
    
    if(data["status"]=="Online"): UI.ui.CMBBOX_Status.setCurrentIndex(0)
    elif(data["status"]=="Idle"): UI.ui.CMBBOX_Status.setCurrentIndex(1)
    elif(data["status"]=="DND"): UI.ui.CMBBOX_Status.setCurrentIndex(2)
    elif(data["status"]=="Invisible"): UI.ui.CMBBOX_Status.setCurrentIndex(3)
    
    UI.ui.PRGRSBAR_CurrentStep.setValue(0)
    UI.ui.PRGRSBAR_CurrentStep.setMaximum(len(data["animation"]))
    
    #UI.ui.LNEDIT_APIToken.setText(data["authToken"])
    
    for i in range(len(data["animation"])):
        UI.ui.TBLW_main.setItem(i, 0, QtWidgets.QTableWidgetItem(data["animation"][i]["text"]))
        UI.ui.TBLW_main.setItem(i, 1, QtWidgets.QTableWidgetItem(data["animation"][i]["emoji_name"]))
        UI.ui.TBLW_main.setItem(i, 2, QtWidgets.QTableWidgetItem(data["animation"][i]["status"]))
        UI.ui.TBLW_main.setItem(i, 3, QtWidgets.QTableWidgetItem(data["animation"][i]["timer"]))
        

def SHAPI():
    if(UI.ui.CHKBOX_APIToken.isChecked()==True):
        UI.ui.LNEDIT_APIToken.setEchoMode(QtWidgets.QLineEdit.EchoMode(0))
    elif(UI.ui.CHKBOX_APIToken.isChecked()==False):
        UI.ui.LNEDIT_APIToken.setEchoMode(QtWidgets.QLineEdit.EchoMode(2))
        
        
def savejson():
    data = {
             "timer": 15,
             "status": "",
             "animation": []
            }
    data["timer"] = UI.ui.SPNBOX_Time.value()
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
    with open(f"Profiles\{UI.ui.CMBBOX_SelectProfile.currentText()}.AMDS-prfl.kfx", "w+") as json_file: json.dump(data, json_file)
        
    
def addline():
    UI.ui.TBLW_main.setRowCount(UI.ui.TBLW_main.rowCount()+1)
    
def deleteline():
    UI.ui.TBLW_main.setRowCount(UI.ui.TBLW_main.rowCount()-1)
    
def opengithub():
    os.startfile("https://github.com/KuFoX-kfx/AMDS")
    
def off():
    try: quit()
    except: sys.exit()
    
    
    
def CreateNewProfile():
    data = {
             "timer": 15,
             "status": "Online",
             "animation": []
             }
    with open(f"Profiles/{UI.ui.CMBBOX_SelectProfile.currentText()}.AMDS-prfl.kfx", "w+", encoding="utf8") as json_file: json.dump(data, json_file)
    ImportSettings()
    
    
def SaveSettings():
    data = {
        "API_Token": None
    }
    
    data["API_Token"] = UI.ui.LNEDIT_APIToken.text()
        
    with open("AMDS-cfg.kfx", "w+", encoding="utf8") as json_file: json.dump(data, json_file)
    
def ImportSettings():
    try:
        #Open Settings
        with open("AMDS-cfg.kfx", "r", encoding="utf8") as json_file: cfg = json.load(json_file)
    except:
        #Create Settings
        cfg = {
        "API_Token": None
                }
        with open("AMDS-cfg.kfx", "w+", encoding="utf8") as json_file:        
            json.dump(cfg, json_file)
    try: 
        with open("Profiles/Default.AMDS-prfl.kfx", "r", encoding="utf8") as json_file: data = json.load(json_file)
    except:
        data = {
                 "timer": 15,
                 "status": "Online",
                 "animation": [{"text": "AMDS By KuFoX", "emoji_name": "\u2139\ufe0f", "status": None, "timer": None}, {"text": "You can download on GitHub", "emoji_name": "\u2139\ufe0f", "status": None, "timer": None}]
                 }
        with open("Profiles/Default.AMDS-prfl.kfx", "w+", encoding="utf8") as json_file:        
            json.dump(data, json_file)
    
    UI.ui.CMBBOX_SelectProfile.clear()
    for i in os.listdir("Profiles/"):
        if('.'.join(i.split('.')[1:]) == "AMDS-prfl.kfx"):
            UI.ui.CMBBOX_SelectProfile.addItem('.'.join(i.split('.')[:1]))
    #Display settings
    UI.ui.LNEDIT_APIToken.setText(cfg["API_Token"])
    
    
def ExportProfile():
    filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "Desktop", "AMDS Profile file (*.AMDS-prfl.kfx)")
    if filename:
        with open(filename, 'w') as file:
            file.write("Welcome to GeeksCoders.com")
            
def ImportProfile():
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", ".", "AMDS Profile file (*.AMDS-prfl.kfx)")
    if filename:
        with open(filename, 'r') as file:
            contents = file.read()
        print(contents)

    
#thr_gui = threading.Thread(target=UI.show())





def startmain():
    UI.ui.PSHBTN_Update.clicked.connect(update_profile)
    UI.ui.PSHBTN_Save.clicked.connect(savejson)
    UI.ui.CHKBOX_APIToken.stateChanged.connect(SHAPI)
    UI.ui.PSHBTN_Add.clicked.connect(addline)
    UI.ui.PSHBTN_Delete.clicked.connect(deleteline)
    UI.ui.ACT_GitHubPage.triggered.connect(opengithub)
    UI.ui.ACT_EXIT.triggered.connect(off)
    UI.ui.CMBBOX_SelectProfile.currentIndexChanged.connect(update_profile)
    UI.ui.PSHBTN_NewProfile.clicked.connect(CreateNewProfile)
    UI.ui.PSHBTN_SaveSettings.clicked.connect(SaveSettings)
    UI.ui.PSHBTN_UpdateSettings.clicked.connect(ImportSettings)
    UI.ui.actionExport_Profile.triggered.connect(ExportProfile)
    UI.ui.actionLoad_Profile.triggered.connect(ImportProfile)
    
       
    thr_animatestatus = threading.Thread(target=AnimateStatus, name="animatestatus")

    ImportSettings()
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