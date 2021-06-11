import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 400, 600)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setWindowOpacity(0.5) #give Opacity from 0-1

app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()