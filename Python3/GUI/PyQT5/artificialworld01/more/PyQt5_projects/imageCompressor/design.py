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
        self.bubble=QtWidgets.QFrame(self)
        self.bubble.setObjectName('bubble')
        self.bubble.move(50, 100)
        self.bubble.mousePressEvent=self.bubble_clicked

        self.dir_bubble=QtWidgets.QPushButton(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)
        self.dir_bubble.mousePressEvent=self.dir_clicked

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

        ##add QLabel
        self.bubble_heading=QtWidgets.QLabel(self.bubble_expanded)
        self.bubble_heading.setText('Compress Image')
        self.bubble_heading.setObjectName('bubble_heading')
        self.bubble_heading.move(95, 8)

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

        self.select_image_label=QtWidgets.QLabel(self.bubble_expanded)
        self.select_image_label.setText('Choose Image')
        self.select_image_label.setObjectName('bubble_para')
        self.select_image_label.move(30, 50)
        
        self.image_path=QtWidgets.QLineEdit(self.bubble_expanded)
        self.image_path.setObjectName('path_text')
        self.image_path.move(60, 85)

        self.select_image_quality=QtWidgets.QLabel(self.bubble_expanded)
        self.select_image_quality.setText('Choose Quality')
        self.select_image_quality.setObjectName('bubble_para')
        self.select_image_quality.move(30, 130)
        
        self.quality_path=QtWidgets.QLineEdit(self.bubble_expanded)
        self.quality_path.setObjectName('quality_path')
        self.quality_path.move(60, 160)

        self.browse_button=QtWidgets.QPushButton(self.bubble_expanded)
        self.browse_button.setText('...')
        self.browse_button.move(240, 85)
        self.browse_button.setObjectName('browse_button')

        self.compress_image=QtWidgets.QPushButton(self.bubble_expanded)
        self.compress_image.setText('Compress')
        self.compress_image.move(108, 260)
        self.compress_image.setObjectName('compress_button')

        ##End Main window

##-------------------------------------------------Functions
    def bubble_clicked(self, event):
        self.bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.bubble_expanded.setVisible(True)

    def dir_clicked(self, event):
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