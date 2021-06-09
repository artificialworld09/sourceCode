import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Geekscoders.com')
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_labels()

    def create_labels(self):
        lbl=QLabel('Label-1', self)
        lbl.setGeometry(10,10, 100, 50) #setGeometry(x,y,w,h)

app=QApplication(sys.argv)
root=Window()
root.show()
sys.exit(app.exec_())