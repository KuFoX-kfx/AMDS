import sys
import threading
from PyQt5 import QtWidgets, QtGui
import time
import Discord_API
import json

from PyQt5 import QtCore, QtGui, QtWidgets


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent):
        self.animate = True
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Animate my discord status')
        
        self.menu = QtWidgets.QMenu(parent)
        self.menu.addAction("AMDS By KuFoX").setEnabled(False)
        
        self.menu.addSeparator()

        self.settings = self.menu.addAction("Open Settings")
        self.settings.setIcon(QtGui.QIcon("icon.png"))

        self.startbtn = self.menu.addAction("Start")
        self.startbtn.setIcon(QtGui.QIcon("icon.png"))
        
        self.stopbtn = self.menu.addAction("Stop")
        self.stopbtn.setIcon(QtGui.QIcon("icon.png"))

        self.menu.addSeparator()
        self.setContextMenu(self.menu)
        #self.activated.connect(self.onTrayIconActivated)
        
        self.startbtn.triggered.connect(self.setstart)
        self.stopbtn.triggered.connect(self.setstop)
        
    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        # if reason == self.Trigger:
        #     self.open_notepad()

    def setstart(self):
        self.animate = True
        self.startbtn.setEnabled(False)
        self.stopbtn.setEnabled(True)
        
    def setstop(self):
        self.animate = False
        self.startbtn.setEnabled(True)
        self.stopbtn.setEnabled(False)
                
    
    
    

        
def start():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    global tray_icon
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('Animate my discord status', 'Start the AMDS')
    
    sys.exit(app.exec_())
    
def getanimate():
    return SystemTrayIcon.animate
    

        
        
