'''
pip3 install PyQt5
sudo apt install python3-pyqt5 (for Linux)

x=left to right
y=top to bottom
width=width of window
height=height of window

self.setGeometry(x,y,width,height)

to fixed window size
self.setFixedHeight(600) #to fixed height
self.setFixedWidth(400) #to fixed width
self.setFixedSize(500, 800) #to set both
'''

'''
QDialog, QWidget, QMainWindow

QWidget: You can't add status bar, main-window etc.
QMainWindow: You can add status bar, main-window etc.

app=QApplication(sys.argv) or 
app=QApplication([])
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()

# sys.exit(app.exec_())