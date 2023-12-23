# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(460, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TBLW_main = QtWidgets.QTableWidget(self.centralwidget)
        self.TBLW_main.setGeometry(QtCore.QRect(10, 10, 441, 151))
        self.TBLW_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TBLW_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TBLW_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TBLW_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TBLW_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TBLW_main.setGridStyle(QtCore.Qt.SolidLine)
        self.TBLW_main.setRowCount(1)
        self.TBLW_main.setObjectName("TBLW_main")
        self.TBLW_main.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.TBLW_main.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBLW_main.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBLW_main.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBLW_main.setHorizontalHeaderItem(3, item)
        self.TBLW_main.horizontalHeader().setVisible(True)
        self.TBLW_main.horizontalHeader().setCascadingSectionResizes(False)
        self.TBLW_main.horizontalHeader().setDefaultSectionSize(100)
        self.TBLW_main.horizontalHeader().setMinimumSectionSize(39)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 200, 131, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 111, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.CMBBOX_Status = QtWidgets.QComboBox(self.centralwidget)
        self.CMBBOX_Status.setGeometry(QtCore.QRect(130, 170, 71, 22))
        self.CMBBOX_Status.setObjectName("CMBBOX_Status")
        self.CMBBOX_Status.addItem("")
        self.CMBBOX_Status.addItem("")
        self.CMBBOX_Status.addItem("")
        self.CMBBOX_Status.addItem("")
        self.PSHBTN_Start = QtWidgets.QPushButton(self.centralwidget)
        self.PSHBTN_Start.setGeometry(QtCore.QRect(380, 200, 75, 23))
        self.PSHBTN_Start.setObjectName("PSHBTN_Start")
        self.PSHBTN_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.PSHBTN_Stop.setGeometry(QtCore.QRect(380, 170, 75, 23))
        self.PSHBTN_Stop.setObjectName("PSHBTN_Stop")
        self.PSHBTN_Update = QtWidgets.QPushButton(self.centralwidget)
        self.PSHBTN_Update.setGeometry(QtCore.QRect(270, 200, 75, 23))
        self.PSHBTN_Update.setObjectName("PSHBTN_Update")
        self.PSHBTN_Save = QtWidgets.QPushButton(self.centralwidget)
        self.PSHBTN_Save.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.PSHBTN_Save.setObjectName("PSHBTN_Save")
        self.SPNBOX_Time = QtWidgets.QSpinBox(self.centralwidget)
        self.SPNBOX_Time.setGeometry(QtCore.QRect(150, 200, 51, 22))
        self.SPNBOX_Time.setReadOnly(False)
        self.SPNBOX_Time.setMinimum(15)
        self.SPNBOX_Time.setMaximum(1200)
        self.SPNBOX_Time.setObjectName("SPNBOX_Time")
        self.PRGRSBAR_CurrentStep = QtWidgets.QProgressBar(self.centralwidget)
        self.PRGRSBAR_CurrentStep.setGeometry(QtCore.QRect(350, 170, 21, 51))
        self.PRGRSBAR_CurrentStep.setMaximum(50)
        self.PRGRSBAR_CurrentStep.setProperty("value", 25)
        self.PRGRSBAR_CurrentStep.setTextVisible(False)
        self.PRGRSBAR_CurrentStep.setOrientation(QtCore.Qt.Vertical)
        self.PRGRSBAR_CurrentStep.setInvertedAppearance(False)
        self.PRGRSBAR_CurrentStep.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.PRGRSBAR_CurrentStep.setObjectName("PRGRSBAR_CurrentStep")
        self.label.raise_()
        self.label_2.raise_()
        self.CMBBOX_Status.raise_()
        self.TBLW_main.raise_()
        self.PSHBTN_Start.raise_()
        self.PSHBTN_Stop.raise_()
        self.PSHBTN_Update.raise_()
        self.PSHBTN_Save.raise_()
        self.SPNBOX_Time.raise_()
        self.PRGRSBAR_CurrentStep.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menubar.setObjectName("menubar")
        self.MN_File = QtWidgets.QMenu(self.menubar)
        self.MN_File.setObjectName("MN_File")
        self.MN_Settings = QtWidgets.QMenu(self.menubar)
        self.MN_Settings.setObjectName("MN_Settings")
        MainWindow.setMenuBar(self.menubar)
        self.ACT_EXIT = QtWidgets.QAction(MainWindow)
        self.ACT_EXIT.setObjectName("ACT_EXIT")
        self.ACT_RunOnStartup = QtWidgets.QAction(MainWindow)
        self.ACT_RunOnStartup.setObjectName("ACT_RunOnStartup")
        self.ACT_RunMinimized = QtWidgets.QAction(MainWindow)
        self.ACT_RunMinimized.setObjectName("ACT_RunMinimized")
        self.ACT_Autostart = QtWidgets.QAction(MainWindow)
        self.ACT_Autostart.setObjectName("ACT_Autostart")
        self.ACT_CheckUpdates = QtWidgets.QAction(MainWindow)
        self.ACT_CheckUpdates.setObjectName("ACT_CheckUpdates")
        self.ACT_Language = QtWidgets.QAction(MainWindow)
        self.ACT_Language.setObjectName("ACT_Language")
        self.ACT_GitHubPage = QtWidgets.QAction(MainWindow)
        self.ACT_GitHubPage.setObjectName("ACT_GitHubPage")
        self.MN_File.addAction(self.ACT_GitHubPage)
        self.MN_File.addAction(self.ACT_EXIT)
        self.MN_Settings.addAction(self.ACT_RunOnStartup)
        self.MN_Settings.addAction(self.ACT_RunMinimized)
        self.MN_Settings.addSeparator()
        self.MN_Settings.addAction(self.ACT_Autostart)
        self.MN_Settings.addSeparator()
        self.MN_Settings.addAction(self.ACT_CheckUpdates)
        self.MN_Settings.addSeparator()
        self.MN_Settings.addAction(self.ACT_Language)
        self.menubar.addAction(self.MN_File.menuAction())
        self.menubar.addAction(self.MN_Settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMDS"))
        item = self.TBLW_main.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Text"))
        item = self.TBLW_main.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Emoji"))
        item = self.TBLW_main.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.TBLW_main.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Default Time(seconds):"))
        self.label_2.setText(_translate("MainWindow", "Default Status:"))
        self.CMBBOX_Status.setItemText(0, _translate("MainWindow", "Online"))
        self.CMBBOX_Status.setItemText(1, _translate("MainWindow", "Idle"))
        self.CMBBOX_Status.setItemText(2, _translate("MainWindow", "DND"))
        self.CMBBOX_Status.setItemText(3, _translate("MainWindow", "Invisible"))
        self.PSHBTN_Start.setText(_translate("MainWindow", "Start"))
        self.PSHBTN_Stop.setText(_translate("MainWindow", "Stop"))
        self.PSHBTN_Update.setText(_translate("MainWindow", "Update"))
        self.PSHBTN_Save.setText(_translate("MainWindow", "Save"))
        self.MN_File.setTitle(_translate("MainWindow", "File"))
        self.MN_Settings.setTitle(_translate("MainWindow", "Settings"))
        self.ACT_EXIT.setText(_translate("MainWindow", "EXIT"))
        self.ACT_RunOnStartup.setText(_translate("MainWindow", "Run On Startup"))
        self.ACT_RunMinimized.setText(_translate("MainWindow", "Run Minimized"))
        self.ACT_Autostart.setText(_translate("MainWindow", "Autostart"))
        self.ACT_CheckUpdates.setText(_translate("MainWindow", "Check Updates"))
        self.ACT_Language.setText(_translate("MainWindow", "Language"))
        self.ACT_GitHubPage.setText(_translate("MainWindow", "Github Page"))
