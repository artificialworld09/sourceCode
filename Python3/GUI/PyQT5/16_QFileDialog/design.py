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

        self.ent=QtWidgets.QLineEdit(self)
        self.ent.setGeometry(10, 10, 300, 35)
        self.ent.setObjectName('select_file')

        self.ent2=QtWidgets.QLineEdit(self)
        self.ent2.setGeometry(10, 70, 300, 35)
        self.ent2.setObjectName('select_dir')

        self.btn1=QtWidgets.QPushButton("...", self)
        self.btn1.setGeometry(320, 10, 70, 35)
        self.btn1.setObjectName("select_file")
        self.btn1.clicked.connect(self.select_file)

        self.btn2=QtWidgets.QPushButton("...", self)
        self.btn2.setGeometry(320, 70, 70, 35)
        self.btn2.setObjectName("select_dir")
        self.btn2.clicked.connect(self.select_dir)
    
    def select_file(self, event):
        fileName, _=QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);; JPEG (*.jpeg);; JPG (*.jpg)")
        self.ent.setText(fileName)
    
    def select_dir(self, event):
        folder=QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ent2.setText(folder)

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()