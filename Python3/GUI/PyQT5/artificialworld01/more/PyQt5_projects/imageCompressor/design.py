import sys
import style
from PyQt5.Qt import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1200, 10, 400, 600)
        self.setWindowTitle('Image_compressor')
        self.setWindowIcon(QIcon('python_1.png'))

        ##to add an external file for designing
        self.setObjectName('main')
        self.setStyleSheet(style.s)

        ##Main window (add a Frames)
        self.bubble=QtWidgets.QPushButton(self)
        self.bubble.setObjectName('bubble')
        self.bubble.move(50, 100)
        self.bubble.clicked.connect(self.bubble_clicked)

        self.dir_bubble=QtWidgets.QPushButton(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)
        self.dir_bubble.clicked.connect(self.dir_clicked)

        ##add QLabel
        self.bubble_heading=QtWidgets.QLabel(self.bubble)
        self.bubble_heading.setText('Compress Image')
        self.bubble_heading.setObjectName('bubble_heading')
        self.bubble_heading.move(95, 8)

        self.dir_bubble_heading=QtWidgets.QLabel(self.dir_bubble)
        self.dir_bubble_heading.setText('Compress multiple images')
        self.dir_bubble_heading.setObjectName('bubble_heading')
        self.dir_bubble_heading.move(60, 8)


        self.bubble_para=QtWidgets.QLabel(self.bubble)
        self.bubble_para.setText('Compress Image')
        self.bubble_para.setObjectName('bubble_para')
        self.bubble_para.move(25, 32)

        self.dir_bubble_para=QtWidgets.QLabel(self.dir_bubble)
        self.dir_bubble_para.setText('Want to compress multiple images at once? select the folder and get compressed version of the images in another folder')
        self.dir_bubble_para.setObjectName('bubble_para')
        self.dir_bubble_para.setWordWrap(True) #to WordWrap
        self.dir_bubble_para.move(10, 32)

        ##bubble_expanded
        self.bubble_expanded=QtWidgets.QFrame(self)
        self.bubble_expanded.setObjectName('bubble_expanded')
        self.bubble_expanded.move(50, 100)
        self.bubble_expanded.setVisible(False)
        self.bubble_expanded.mousePressEvent=self.back_arrow_clicked

        ##dir_bubble_expanded
        self.dir_bubble_expanded=QtWidgets.QFrame(self)
        self.dir_bubble_expanded.setObjectName('bubble_expanded')
        self.dir_bubble_expanded.move(50, 100)
        self.dir_bubble_expanded.setVisible(False)

        ##back Arrow (QLabel)
        self.back_arrow=QtWidgets.QLabel(self.bubble_expanded)
        self.back_arrow.move(15, 0)
        self.back_arrow.setObjectName('back_arrow')
        self.back_arrow.setTextFormat(Qt.RichText)
        self.back_arrow.setText('&#8592;')
        self.back_arrow.mousePressEvent=self.back_arrow_clicked


        self.dir_back_arrow=QtWidgets.QLabel(self.dir_bubble_expanded)
        self.dir_back_arrow.move(15, 0)
        self.dir_back_arrow.setObjectName('back_arrow')
        self.dir_back_arrow.setTextFormat(Qt.RichText)
        self.dir_back_arrow.setText('&#8592;')
        self.dir_back_arrow.mousePressEvent=self.back_arrow_clicked

        ##text (QLabel)
        self.bubble_expanded_para=QtWidgets.QLabel(self.bubble_expanded)
        self.bubble_expanded_para.move(10, 30)
        self.bubble_expanded_para.setText('This is bubble_expanded para')

        self.dir_bubble_expanded_para=QtWidgets.QLabel(self.dir_bubble_expanded)
        self.dir_bubble_expanded_para.move(10, 30)
        self.dir_bubble_expanded_para.setText('This is dir_bubble_expanded para')

        ##End Main window

##-------------------------------------------------Functions
    def bubble_clicked(self):
        self.bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.bubble_expanded.setVisible(True)

    def dir_clicked(self):
        self.bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.dir_bubble_expanded.setVisible(True)

    def back_arrow_clicked(self, event):
        self.bubble.setVisible(True)
        self.dir_bubble.setVisible(True)
        self.bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(False)


app=QApplication(sys.argv)
root=App()
root.show()
app.exec_()