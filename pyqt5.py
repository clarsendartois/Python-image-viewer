from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 300, 300)
    win.setWindowTitle("Tech Wiht Tim!")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


window()
# 2.PyQt5 Tutorial - Buttons and Events (Signals)
