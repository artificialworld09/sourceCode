import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 400, 600)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('images/python.png'))

        ##to add an external file for designing
        self.setObjectName('main_window')
        stylesheet=''
        with open('design.qss','r') as f:
            stylesheet=f.read()
        self.setStyleSheet(stylesheet)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()