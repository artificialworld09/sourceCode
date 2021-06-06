'''
self.setFixedWidth(400) #to fix the width.
self.setFixedHeight(300) #to fix the height.


##to set both
self.setFixedSize(400, 800) #width, height

self.height=600
self.width=400
self.setFixedSize(self.width, self.height)

25:00/7:05:01
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setFixedSize(400, 300)

        self.show()

app=QApplication(sys.argv)
root=Window()
sys.exit(app.exec_())