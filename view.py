from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Yotube downloader')
        self.setGeometry(600, 300, 450, 300)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('My Youtube downloader')
        self.main_text.move(150, 10)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(170, 250)
        self.btn.setText("Жмякни сюда")
        self.btn.setFixedWidth(120)
        self.btn.clicked.connect(self.btn_click)


def btn_click():
    print('Test')


def app_window():
    app = QApplication(sys.argv)
    window = QMainWindow()


    window.show()
    sys.exit(app.exec_())