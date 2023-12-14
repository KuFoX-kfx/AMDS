#pyuic5 gui.ui -o gui.py
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys
import time
import os

app = QtWidgets.QApplication(sys.argv)
STRT = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(STRT)
STRT.show()

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def run(self):
        """Long-running task."""
        time.sleep(1)
        ui.pushButton.setEnabled(True)
        self.finished.emit()
        

def Lmao():
    thread = QThread(parent=STRT)
    # Step 3: Create a worker object
    worker = Worker()
    # Step 4: Move worker to the thread
    worker.moveToThread(thread)
    # Step 5: Connect signals and slots
    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.finished.connect(lambda: ui.pushButton.setEnabled(True))
    thread.finished.connect(lambda: ui.pushButton.setText("Finish"))
    # Step 6: Start the thread
    thread.start()
    ui.pushButton.setEnabled(False)
    
    
    
    

ui.pushButton.clicked.connect(Lmao)

sys.exit(app.exec_())