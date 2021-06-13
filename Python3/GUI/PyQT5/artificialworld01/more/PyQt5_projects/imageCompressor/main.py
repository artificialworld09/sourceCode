import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import design

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 400, 600)
        self.setWindowTitle('Image_compressor')
        self.setWindowIcon(QIcon('python_1.png'))

        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(design.s)

        ##Main window (add a Frames)
        self.bubble=QtWidgets.QPushButton(self)
        self.bubble.setObjectName('bubble')
        self.bubble.move(50, 100)
        self.bubble.clicked.connect(self.clicked)

        self.dir_bubble=QtWidgets.QPushButton(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)
        self.dir_bubble.clicked.connect(self.clicked)
        ##End Main window

##-------------------------------------------------Functions
    def clicked(self):
        self.bubble.setVisible(False)
        self.dir_bubble.setVisible(False)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()