import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left=10
        self.top=10
        self.width=400
        self.height=600
        self.setFixedSize(self.width, self.height) #to set both
        self.title='Main Window'
        ##to add an external file for designing
        self.setObjectName('main_window') #to access in css file
        stylesheet=''
        with open('design.css','r') as f:
            stylesheet=f.read()
        self.setStyleSheet(stylesheet)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        ##Main window (add a Frames)
        self.bubble=QFrame(self)
        self.bubble.setObjectName('bubble')
        self.bubble.move(50, 100)

        self.dir_bubble=QFrame(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)

        ##-----------------------------------------Label
        self.b_heading=QLabel(self.bubble)
        self.b_heading.setText('Compress Image')
        self.b_heading.setObjectName('heading')
        self.b_heading.move(100,8)

        self.dir_heading=QLabel(self.dir_bubble)
        self.dir_heading.setText('Compress multiple')
        self.dir_heading.setObjectName('heading')
        self.dir_heading.move(100,8)

        self.b_para=QLabel(self.bubble)
        self.b_para.setText('Click here to compresss single image!')
        self.b_para.setObjectName('para')
        self.b_para.move(25, 32)

        self.dir_para=QLabel(self.dir_bubble)
        self.dir_para.setText('Click here and select folder to compresss multiple images!')
        self.dir_para.setObjectName('para')
        self.dir_para.setWordWrap(True);
        self.dir_para.move(10, 32)


        ##End Main window

        self.show()

##-------------------------------------------------Functions
def bubble_clicked(self):
    print('bubble clicked!!!')

def dir_bubble_clicked(self):
    print('dir_bubble clicked!!!')

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())


##04:44/17:46