# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\micha\OneDrive\Escritorio\GitHub\PyQt5_designer_basics\images_QPixMap\images_QPixMap_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(6, 2, 571, 321))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../data/46279.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.wallpaper_I = QtWidgets.QPushButton(self.centralwidget)
        self.wallpaper_I.setGeometry(QtCore.QRect(84, 330, 151, 23))
        self.wallpaper_I.setObjectName("wallpaper_I")
        self.wallpaper_II = QtWidgets.QPushButton(self.centralwidget)
        self.wallpaper_II.setGeometry(QtCore.QRect(320, 330, 141, 23))
        self.wallpaper_II.setObjectName("wallpaper_II")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.wallpaper_I.clicked.connect(self.show_wallpaperI)
        self.wallpaper_II.clicked.connect(self.show_wallpaperII)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wallpaper_I.setText(_translate("MainWindow", "Wallpaper I"))
        self.wallpaper_II.setText(_translate("MainWindow", "Wallpaper II"))
        
    def show_wallpaperI(self):
        self.photo.setPixmap(QtGui.QPixmap("data/46279.jpg"))
        
    def show_wallpaperII(self):
        self.photo.setPixmap(QtGui.QPixmap("data/thumb-350-909663.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

