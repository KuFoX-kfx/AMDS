import sys
import threading
from PyQt5 import QtWidgets, QtGui


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Animate my discord status')
        menu = QtWidgets.QMenu(parent)
        menu.addAction("AMDS By KuFoX").setEnabled(False)
        
        menu.addSeparator()

        settings = menu.addAction("Open Settings")
        settings.triggered.connect(self.activate_ui)
        settings.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

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
