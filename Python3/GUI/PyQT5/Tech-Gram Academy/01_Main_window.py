'''
https://pythonspot.com/pyqt5/

sudo apt install python3-pyqt5 (for Linux)

to fixed window size
self.setFixedHeight(600) #to fixed height
self.setFixedWidth(400) #to fixed width
self.setFixedSize(self.width, self.height) #to set both
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, #QWidget
'''
QWidget: You can't add status bar, main-window etc.
QMainWindow: You can add status bar, main-window etc.
'''
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left=30
        self.top=100
        self.width=400
        self.height=600
        self.setFixedSize(self.width, self.height) #to set both
        self.title='Main Window'
        self.setStyleSheet('background-color: grey')

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())