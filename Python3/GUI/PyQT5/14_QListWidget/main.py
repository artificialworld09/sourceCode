"""
Topics:
self.list.addItem("Janaury")
self.list.insertItem("Janaury")
self.list.insertItems(["Januaury", "February"])

item=self.list.currentItem().text()

self.list.clicked.connect(self.list_clicked)
self.list.itemClicked.connect(self.list_clicked)
self.list.itemDoubleClicked.connect(self.list_clicked)
"""


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont
import design

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 Signal and slots')
        self.setWindowIcon(QIcon('images/python.png'))
        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(design.s)
        self.setGeometry(10, 10, 400, 600)

        self.list=QtWidgets.QListWidget(self)
        self.list.move(190, 10)
        self.list.setObjectName('list')

        ##add one item at a time
        # self.list.addItem("Janaury")
        # self.list.addItem("February")
        # self.list.addItem("March")
        # self.list.addItem("April")
        # self.list.addItem("May")
        # self.list.addItem("June")
        # self.list.addItem("July")
        # self.list.addItem("August")
        # self.list.addItem("September")
        # self.list.addItem("October")
        # self.list.addItem("November")
        # self.list.addItem("December")
        
        ##add multiple items at a time
        # self.list.addItems(["Janaury","February","March","April","May","June","July","August","September","October","November","December"])
        
        ##add item by index number
        self.list.insertItem(0, "Janaury")
        self.list.insertItem(2, "February")
        self.list.insertItem(1, "March")
        self.list.insertItem(3, "April")
        self.list.insertItem(4, "May")
        self.list.insertItem(5, "June")
        self.list.insertItem(6, "July")
        self.list.insertItem(7, "August")
        self.list.insertItem(8, "September")
        self.list.insertItem(9, "October")
        self.list.insertItem(10, "November")
        self.list.insertItem(11, "December")

        # self.list.clicked.connect(self.list_clicked) #to perform clicked
        self.list.itemClicked.connect(self.list_clicked) #to perform clicked

        self.lbl=QtWidgets.QLabel(self)
        self.lbl.move(10, 10)
        self.lbl.setFont(QFont("Sanserif", 15))
    
    def list_clicked(self):
        item=self.list.currentItem().text()
        
        self.lbl.setText(item)
        self.lbl.adjustSize()

app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()