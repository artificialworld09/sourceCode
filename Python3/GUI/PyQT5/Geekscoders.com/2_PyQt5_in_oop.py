'''
self.setGeometry(x,y,width,height)
x=left to right
y=top to bottom
width=width of window
height=height of window

QDialog, QWidget, QMainWindow

20:00/7:05:01
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)

        self.show()

app=QApplication(sys.argv)
root=Window()
sys.exit(app.exec_())