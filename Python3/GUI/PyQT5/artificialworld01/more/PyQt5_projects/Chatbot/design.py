from speak import speak
from wish_me import wishMe
import style
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt
import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
per=str(percentage)[0:5]
percent=float(per)


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1320, 10, 600, 1000)
        self.setWindowTitle('QLineEdit & QPushButton')
        self.setWindowIcon(QIcon('python.png'))
        self.setStyleSheet(style.ss)
        self.setObjectName('root')
##QLineEdit
        self.en=QtWidgets.QLineEdit(self)
        self.en.move(10, 960)
        self.en.setObjectName('en')
        self.en.adjustSize()
##QFrame
        self.frm=QtWidgets.QFrame(self)
        self.frm.move(10, 10)
        self.frm.setObjectName('frm')
##QLabel
        self.lbl=QtWidgets.QLabel('', self.frm)
        self.lbl.move(10, 10)
        self.lbl.adjustSize()
        self.lbl.setObjectName('lbl')

    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Return:           
                data=self.en.text()
                data2=data.lower()
                self.lbl.setText(data)
                self.lbl.adjustSize()
                self.en.setText('')

                if data2 in "hi":
                        speak("hello sir!")
                elif data2 in "hello":
                        speak("hi sir!")
                elif data2 in "who are you?":
                        speak("I'm a computer program, my name is Alexa")
                elif data2 in "how are you?":
                        speak("I'm fine sir")
                elif data2 in "what is your name?":
                        speak("My name is Alexa, please tell me how may I help you?")
                elif data2 in "how old are you?":
                        speak("I'm 18 years old now sir!")

                ##battry 
                elif data2 in 'how much battary do we have':
                        if percent>=75:
                                speak('We have enough power to continue our work')
                        elif percent>=40 and percentage<=75:
                                speak('We should connect our system to charging point to charge our battery')
                        elif percent>=15 and percentage<=30:
                                speak("We don't have enough power to work, please connect to charging")
                        elif percent<=15:
                                speak("we have very low power, please connect to charging the system will shutdown very soon")



                elif data2 in "goodbye alexa":
                        speak('Shutting down, thank you sir!')
                        app.destroy()

app=QApplication(sys.argv)
root=App()
root.show()
wishMe()
app.exec_()