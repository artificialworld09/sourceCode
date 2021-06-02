import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import design

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left=30
        self.top=100
        self.width=400
        self.height=600
        self.setFixedSize(self.width, self.height) #to set both
        self.title='Main Window'
        ##to add an external file for designing
        self.setObjectName('main_window')
        self.setStyleSheet(design.ss)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())