import view

if __name__ == "__main__":
    import sys
    app = view.QtWidgets.QApplication(sys.argv)
    MainWindow = view.QtWidgets.QMainWindow()
    ui = view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())