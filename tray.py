import sys
import threading
from PyQt5 import QtWidgets, QtGui


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
        self.start.setIcon(QtGui.QIcon("icon.png"))
        
        self.stop = self.menu.addAction("Stop")
        self.stop.setIcon(QtGui.QIcon("icon.png"))

        self.menu.addSeparator()
        self.setContextMenu(self.menu)
        #self.activated.connect(self.onTrayIconActivated)

    def activate_ui(self):
        from main import import_ui
        threading.Thread(target=lambda: import_ui()).start()
        
    
    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        # if reason == self.Trigger:
        #     self.open_notepad()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('VFX Pipeline', 'Hello "Name of logged in ID')
    sys.exit(app.exec_())
