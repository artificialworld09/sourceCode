import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Geekscoders.com')

        self.show()

app=QApplication(sys.argv)
root=Window()
sys.exit(app.exec_())