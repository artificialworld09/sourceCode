'''
pip3 install PyQt5
sudo apt install python3-pyqt5 (for Linux)
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 400, 600)

app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()