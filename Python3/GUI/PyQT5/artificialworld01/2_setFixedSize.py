'''
self.setFixedWidth(400) #to fix the width.
self.setFixedHeight(600) #to fix the height.

##to set both
self.setFixedSize(400, 600) #width, height
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 600)

app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()