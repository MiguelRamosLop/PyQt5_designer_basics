# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\micha\OneDrive\Escritorio\GitHub\PyQt5_designer_basics\popups_messages_boxes\popupsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(180, 120, 251, 141))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "PushButton"))
        
    def show_popup(self):
        msg = QMessageBox()
        # change the window title
        msg.setWindowTitle("popup")
        msg.setText("popup message")
        
        # different popup icon available
        msg.setIcon(QMessageBox.Information)
        #msg.setIcon(QMessageBox.Warning)
        #msg.setIcon(QMessageBox.Critical)
        #msg.setIcon(QMessageBox.Question)
        
        # the fist button is always the default, it means that the user can press enter to click the button
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # also we can define the default button order
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText("Do you want to save your changes?")
        
        msg.setDetailedText("This is a detailed text")
        
        msg.buttonClicked.connect(self.popup_btn)
        
        x = msg.exec_()

    def popup_btn(self, i):
        # imprimimos en consola el boton que se ha pulsado
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

