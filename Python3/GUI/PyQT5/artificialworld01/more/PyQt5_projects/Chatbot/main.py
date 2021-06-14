from speak import speak
from wish_me import wishMe
import design
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1320, 10, 600, 1000)
        self.setWindowTitle('QLineEdit & QPushButton')
        self.setWindowIcon(QIcon('python.png'))
        self.setStyleSheet(design.ss)
        self.setObjectName('root')
##QLineEdit
        self.en=QtWidgets.QLineEdit(self)
        self.en.move(10, 10)
        self.en.setObjectName('en')
        self.en.adjustSize()
##QPushButton
        self.btn=QtWidgets.QPushButton('ENTER', self)
        self.btn.move(510, 10)
        self.btn.clicked.connect(self.clicked)
        self.btn.adjustSize()
        self.btn.setObjectName('btn')
##QFrame
        self.frm=QtWidgets.QFrame(self)
        self.frm.move(10, 50)
        self.frm.setObjectName('frm')
##QLabel
        self.lbl=QtWidgets.QLabel('', self.frm)
        self.lbl.move(10, 10)
        self.lbl.adjustSize()
        self.lbl.setObjectName('lbl')

##Functions
    def clicked(self):
        data=self.en.text()
        data2=data.lower()
        self.lbl.setText(data)
        self.lbl.adjustSize()
        self.en.setText('')
        if data2 in "who are you?":
                speak("I'm Alexa, please tell me how may I help you?")
        if data2 in "what is your name?":
                speak("My name is Alexa, please tell me how may I help you?")
        if data2 in "hi":
                speak("hello sir!")
        if data2 in "hello":
                speak("hi sir!")
        if data2 in "how old are you?":
                speak("I'm 18 years old now sir!")
        if data2 in "how are you?":
                speak("I'm fine sir")

app=QApplication(sys.argv)
root=App()
root.show()
wishMe()
app.exec_()