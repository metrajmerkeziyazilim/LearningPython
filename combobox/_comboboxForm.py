# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.cbSehirler.setObjectName("cbSehirler")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 47, 13))
        self.label.setObjectName("label")
        self.btnGetItem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(70, 120, 101, 31))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLoadItem.setGeometry(QtCore.QRect(220, 120, 111, 31))
        self.btnLoadItem.setObjectName("btnLoadItem")
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(70, 180, 111, 31))
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItem.setText(_translate("MainWindow", "Load Item"))
        self.btnClear.setText(_translate("MainWindow", "Temizle"))
