'''
doc.qt.io/qt-5/qt.html#Key-enum
enum Qt::Key
The key names used by Qt.

Qt::Key_Escape
Qt::Key_Tab
Qt::Key_Backtab
Qt::Key_Backspace
Qt::Key_Return
Qt::Key_Enter
Qt::Key_Insert
Qt::Key_Delete
Qt::Key_Pause
Qt::Key_Print
Qt::Key_SysReq
Qt::Key_Space

Qt::Key_Clear

Qt::Key_Home
Qt::Key_End

Qt::Key_Left
Qt::Key_Up
Qt::Key_Right
Qt::Key_Down

Qt::Key_PageUp
Qt::Key_PageDown
Qt::Key_Shift
Qt::Key_Control
Qt::Key_Alt
Qt::Key_AltGr
Qt::Key_CapsLock
Qt::Key_NumLock
Qt::Key_ScrollLock

Qt::Key_Meta
Qt::Key_F1 - Qt::Key_F29
'''
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    ##Example-1 (This will show only key event)
    # def keyPressEvent(self, event):
    #     print('Key press event fired!!')
        
    ##Example-2 (This will show key-pressed values)
    # def keyPressEvent(self, event):
    #     print(event.key())
        
    ##Example-3 (This will show key values)
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Return:
            self.test_method()

    def test_method(self):
        print("Enter key pressed")

if __name__=="__main__":
    app=QApplication(sys.argv)
    root=MainWindow()
    root.show()
    sys.exit(app.exec_())