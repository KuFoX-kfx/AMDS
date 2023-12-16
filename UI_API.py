#pyuic5 gui.ui -o gui.py
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UI_API:
    
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.STRT = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.STRT)
        
    def show(self):
        self.STRT.show()
        sys.exit(self.app.exec_())
