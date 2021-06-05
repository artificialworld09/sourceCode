'''
pip3 install PyQt5

11:00/7:05:01
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app=QApplication(sys.argv) # app=QApplication([]), app=QApplication(sys.argv)
root=QWidget()
root.show()
app.exec_()