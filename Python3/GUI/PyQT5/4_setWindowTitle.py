import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 400, 600)
        self.setWindowTitle('Geekscoders.com')

app=QApplication(sys.argv)
root=Window()
root.show()
app.exec_()