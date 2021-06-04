import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
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
        self.bubble.mousePressEvent = bubble_clicked

        self.dir_bubble=QFrame(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)
        self.dir_bubble.mousePressEvent = dir_bubble_clicked #to perform clicked event
        ##End Main window

        self.show()

##-------------------------------------------------Functions
def bubble_clicked(self):
    print('bubble clicked!!!')
    # self.bubble.setVisible(False)

def dir_bubble_clicked(self):
    print('dir_bubble clicked!!!')

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())

'''
6:32/14:29
'''