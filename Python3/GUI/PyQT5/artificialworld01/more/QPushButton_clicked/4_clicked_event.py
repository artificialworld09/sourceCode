import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QLabel
from PyQt5.QtGui import QIcon
import design

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 Signal and slots')
        self.setWindowIcon(QIcon('images/python.png'))
        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(design.s)
        self.setGeometry(10, 10, 400, 600)

        self.lbl1=QLabel('Label1', self)
        self.lbl1.move(10, 10)

        self.create_buttons()
    
    def create_buttons(self):
        btn1=QPushButton('clickMe', self)
        btn1.move(10, 50)
        btn1.clicked.connect(self.clicked_btn)
    
    def clicked_btn(self):
            self.lbl1.setText('Hello world!')
            self.lbl1.setObjectName('label')
            self.lbl1.setStyleSheet(design.s)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()