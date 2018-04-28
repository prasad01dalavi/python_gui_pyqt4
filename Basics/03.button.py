import sys
from PyQt4 import QtGui, QtCore             # QtCore is for adding button


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.button_setting()          # Initialize the button

    def button_setting(self):
        btn = QtGui.QPushButton("Quit", self)    # Give name to the button
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # When button is clicked then (connect to) Quit
        # close the application

        btn.resize(70, 30)       # size of the button (width, height)
        btn.move(210, 150)       # button position (from left, from up)
        self.show()


def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
