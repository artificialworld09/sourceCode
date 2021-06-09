'''
btn1.move(10, 20) #to set only position of button

32:11/7:05:01
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_buttons()
    
    def create_buttons(self):
        btn1=QPushButton('clickMe', self)
        btn1.move(10, 20) #to set only position of button

app=QApplication(sys.argv)
root=Window()
root.show()
sys.exit(app.exec_())