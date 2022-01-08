from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


class MyWindow(QMainWindow):
    # create an init method
    def __init__(self):
        # calling the parent constructor
        super(MyWindow, self).__init__()
        # set the size of the window
        self.setGeometry(100, 100, 300, 300) # x, y, width, height
        self.setWindowTitle("PyQT5 basics")
        self.initUI()
    
    # update the widht of the label
    def update(self):
        self.label.adjustSize()
        
    #create a function where the btn is clicked  
    def clicked(self):
        self.label.setText("The button was clicked!")
        # if the label is too small, update it
        self.update()
    
    # all stuff on the window
    def initUI(self):
         # add some stuff to the window
        self.label = QtWidgets.QLabel(self) 
        self.label.setText("Hello World!")
        # move the label to the center of the window
        self.label.move(100, 100)
        # this is an instance of my window this is why we put the self insted of the window name win
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Click Me!")
        # connect the btn click event to the function
        self.btn.clicked.connect(self.clicked)
    
# define an application
def window():
    # give some config setup for the application
    app = QApplication(sys.argv)
    # create some window/widget instance of the first function
    win = MyWindow()
    # show the window
    win.show()
    sys.exit(app.exec_())
    
window()
