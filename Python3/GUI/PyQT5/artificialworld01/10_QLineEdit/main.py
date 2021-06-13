import design
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1520, 10, 400, 600)
        self.setWindowTitle('QLineEdit & QPushButton')
        self.setWindowIcon(QIcon('../images/python.png'))
        self.setStyleSheet(design.ss)
        self.setObjectName('root')
##QLineEdit
        self.en=QtWidgets.QLineEdit(self)
        self.en.move(10, 10)
        self.en.setObjectName('en')
        self.en.adjustSize()
##QPushButton
        self.btn=QtWidgets.QPushButton('ENTER', self)
        self.btn.move(310, 10)
        self.btn.clicked.connect(self.clicked)
        self.btn.adjustSize()
        self.btn.setObjectName('btn')
##QLabel
        self.lbl=QtWidgets.QLabel('Your text', self)
        self.lbl.move(10, 50)
        self.lbl.adjustSize()
        self.lbl.setObjectName('lbl')

##Functions
    def clicked(self):
        data=self.en.text()
        self.lbl.setText(data)
        self.lbl.adjustSize() #to adjust QLabel data
        self.en.setText('') #to remove QLineEdit data

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()