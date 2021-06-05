'''

25:35/7:05:01
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
        self.setWindowOpacity(0.5) #give Opacity from 0-1

        self.show()

app=QApplication(sys.argv)
root=Window()
sys.exit(app.exec_())