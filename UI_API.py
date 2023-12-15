#pyuic5 gui.ui -o gui.py
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys
import threading
import time
import os

app = QtWidgets.QApplication(sys.argv)
STRT = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(STRT)
STRT.show()


def Run():
    for i in range(10):
        time.sleep(1)
        print(i)
    
def Lmao():
    t1=threading.Thread(target=Run)
    if(t1.is_alive()==False): t1.start()
    

    
    

ui.pushButton.clicked.connect(Lmao)

sys.exit(app.exec_())