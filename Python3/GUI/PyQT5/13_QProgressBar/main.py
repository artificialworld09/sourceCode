import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import style
from PyQt5.QtCore import QBasicTimer

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 ProgressBar')
        self.setWindowIcon(QIcon('images/python.png'))
        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(style.s)
        self.setGeometry(10, 10, 400, 600)

##QProgressBar
        self.pb=QtWidgets.QProgressBar(self)
        self.pb.setGeometry(10, 10, 380, 30)

##QPushButton
        self.btn1=QtWidgets.QPushButton("Start", self)
        self.btn1.move(10, 70)
        self.btn1.clicked.connect(self.start)

        self.btn2=QtWidgets.QPushButton("Reset", self)
        self.btn2.move(290, 70)
        self.btn2.clicked.connect(self.reset)

##QBasicTimer
        self.timer=QBasicTimer()
        self.step=0

##Functions
    def start(self):
        if self.timer.isActive():
                self.timer.stop()
                self.btn1.setText("Start")
        else:
                self.timer.start(100, self)
                self.btn1.setText('Stop')
    def timerEvent(self, event):
        if self.step>=100:
                self.timer.stop()
                self.btn1.setText('Start')
                return
        self.step+=1
        self.pb.setValue(self.step)

    def reset(self):
            self.step=0
            self.pb.setValue(0)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()

##05:19/10:41