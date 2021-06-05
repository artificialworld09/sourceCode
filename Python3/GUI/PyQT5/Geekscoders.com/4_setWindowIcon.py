'''
24:15/7:05:01
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('css.png'))

        self.show()

app=QApplication(sys.argv)
root=Window()
sys.exit(app.exec_())