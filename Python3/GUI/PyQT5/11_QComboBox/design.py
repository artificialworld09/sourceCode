import style
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1520, 10, 400, 600)
        self.setWindowTitle('QComboBox')
        self.setWindowIcon(QIcon('../images/python.png'))
        self.setStyleSheet(style.ss)
        self.setObjectName('root')
##QComboBox
        self.combo=QtWidgets.QComboBox(self)
        self.combo.move(294, 10)
        self.combo.resize(96, 26)
        self.combo.setObjectName('quality_combo')
        self.combo.addItem('High')
        self.combo.addItem('Medium')
        self.combo.addItem('Low')
        self.combo.currentIndexChanged.connect(self.select_value)
##QLineEdit
        self.path=QtWidgets.QLineEdit(self)
        self.path.move(10, 10)
        self.path.resize(250, 26)
        self.path.setObjectName('en')

##QLabel
        self.lbl=QtWidgets.QLabel(self)
        self.lbl.move(10, 40)
        self.lbl.setText('para')
        self.lbl.setObjectName('para')
        self.lbl.adjustSize()

##QPushButton
        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText('Click me')
        self.btn.move(10, 70)
        self.btn.resize(96, 26)
        self.btn.setObjectName('btn')
        self.btn.clicked.connect(self.Print_me)


##Functions
    def select_value(self):
            if self.combo.currentText()=='High':
                    self.path.setText('You have selected High')
            
            elif self.combo.currentText()=='Medium':
                    self.path.setText('You have selected Medium')
            
            elif self.combo.currentText()=='Low':
                    self.path.setText('You have selected Low')

    def Print_me(self):
            data=self.path.text()
            if data=='You have selected High':
                    self.lbl.setText(data)
                    self.lbl.adjustSize()
            elif data=='You have selected Medium':
                    self.lbl.setText(data)
                    self.lbl.adjustSize()
            elif data=='You have selected Low':
                    self.lbl.setText(data)
                    self.lbl.adjustSize()
            else:
                    self.lbl.setText("You have selected wrong data")  
                    self.lbl.adjustSize()  

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()