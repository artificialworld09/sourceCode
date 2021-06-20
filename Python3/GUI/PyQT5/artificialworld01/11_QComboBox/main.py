import design
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
        self.setStyleSheet(design.ss)
        self.setObjectName('root')
##QComboBox
        self.quality_combo=QtWidgets.QComboBox(self)
        self.quality_combo.move(170, 160)
        self.quality_combo.resize(96, 26)
        self.quality_combo.setObjectName('quality_combo')
        self.quality_combo.addItem('High')
        self.quality_combo.addItem('Medium')
        self.quality_combo.addItem('Low')

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()