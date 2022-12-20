from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def app_window():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Yotube downloader')
    window.setGeometry(600, 300, 450, 300)

    window.show()
    sys.exit(app.exec_())