import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont
import style

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 Signal and slots')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setGeometry(10, 10, 400, 600)
        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(style.s)

        self.frm=QtWidgets.QFrame(self)
        self.frm.setGeometry(190, 10, 200, 550)
        self.frm.move(190, 10)
        self.frm.setObjectName('frm')
        self.frm.mousePressEvent=self.clicked

        self.frm2=QtWidgets.QFrame(self)
        self.frm2.setGeometry(10, 10, 200, 550)
        self.frm2.setObjectName('frm')
        self.frm2.setVisible(False)
        self.frm2.mousePressEvent=self.clicked2
    
    def clicked(self, event):
        self.frm.setVisible(False)
        self.frm2.setVisible(True)
    
    def clicked2(self, event):
        self.frm.setVisible(True)
        self.frm2.setVisible(False)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()