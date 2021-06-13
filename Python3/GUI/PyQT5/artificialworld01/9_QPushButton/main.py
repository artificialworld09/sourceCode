import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import design

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 Signal and slots')
        self.setWindowIcon(QIcon('images/python.png'))
        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(design.s)
        self.setGeometry(10, 10, 400, 600)

        self.lbl=QtWidgets.QLabel('Label1', self)
        self.lbl.move(10, 10)

        self.create_buttons()
    
    def create_buttons(self):
        btn1=QtWidgets.QPushButton('clickMe', self)
        btn1.move(10, 50)
        btn1.clicked.connect(self.clicked_btn)
    
    def clicked_btn(self):
        self.lbl.setText('Hello world! how are you?')
        self.lbl.adjustSize() #to auto-adjust textWidth

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()