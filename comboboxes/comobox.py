# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\micha\OneDrive\Escritorio\GitHub\PyQt5_designer_basics\comboboxes\comoboxGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboX = QtWidgets.QComboBox(self.centralwidget)
        self.comboX.setGeometry(QtCore.QRect(30, 50, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboX.setFont(font)
        self.comboX.setObjectName("comboX")
        self.comboX.addItem("")
        self.comboX.addItem("")
        self.comboY = QtWidgets.QComboBox(self.centralwidget)
        self.comboY.setGeometry(QtCore.QRect(290, 50, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboY.setFont(font)
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(190, 260, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # añadir un item al combobox
        self.comboX.addItem("Item añadido")
        # modificar un item del combobox
        index = self.comboX.findText("Item añadido", QtCore.Qt.MatchFixedString)
        self.comboX.setCurrentIndex(index)
        
        self.submit.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboX.setItemText(0, _translate("MainWindow", "0"))
        self.comboX.setItemText(1, _translate("MainWindow", "1"))
        self.comboY.setItemText(0, _translate("MainWindow", "1"))
        self.comboY.setItemText(1, _translate("MainWindow", "0"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X XOR Y = "))
        
    def pressed(self):
        # provide what is the actual value of the combobox
        x = int(self.comboX.currentText())
        y = int(self.comboY.currentText())
        xor = (x and not y) or (not x and y)
        if xor == True:
            xor = 1
        else:
            xor = 0
        
        self.label.setText("X XOR Y = " + str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

