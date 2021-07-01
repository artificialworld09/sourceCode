"""
from PyQt5.QtGui import QFont
self.lbl2.setWordWrap(True)
"""

import style
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 10, 1200, 800)
        self.setWindowTitle('ArtificialWorld01.in')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setStyleSheet('background-color: green')
        self.setStyleSheet(style.ss)

##QFrame
        self.frm1=QtWidgets.QFrame(self)
        self.frm1.setGeometry(10, 10, 500, 780)
        self.frm1.setObjectName('fr')

        self.frm2=QtWidgets.QFrame(self)
        self.frm2.setGeometry(690, 10, 500, 780)
        self.frm2.setObjectName('fr')
        self.frm1.setStyleSheet('background-color: gray')

##QLabel
        self.lbl1=QtWidgets.QLabel(self.frm1)
        self.lbl1.move(0, 0)
        self.lbl1.setWordWrap(True)
        self.lbl1.setObjectName('lb')
        self.setFont(QFont("Times New Roman", 15))
        self.lbl1.setText('''Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quibusdam temporibus eum illum, dicta, dolorem blanditiis libero earum repudiandae a possimus repellendus impedit? Modi quod totam dignissimos blanditiis culpa quis.consectetur maiores repudiandae, provident natus! Inventore, assumenda!''')

        self.lbl2=QtWidgets.QLabel(self.frm2)
        self.lbl2.move(0, 0)
        self.lbl2.setWordWrap(True)
        self.lbl2.setObjectName('lb')
        self.lbl2.setFont(QFont("Times New Roman", 25))
        self.lbl2.setText('''Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quibusdam temporibus eum illum, dicta, dolorem blanditiis libero earum repudiandae a possimus repellendus impedit? Modi quod totam dignissimos blanditiis culpa quis.consectetur maiores repudiandae, provident natus! Inventore, assumenda!''')


app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()