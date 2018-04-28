import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        self.button_setting()

    def button_setting(self):
        btn = QtGui.QPushButton("Button", self)  # Name of Button
        btn.clicked.connect(self.button_message)
        # Call method buttonMessage when the button is clicked
        btn.resize(70, 30)         # Size of the button (can be default)
        btn.move(210, 150)         # Button position (from left, from up)
        self.show()

    def button_message(self):
        print "Button is pressed"
        # When button is clicked. We get the message on Python Shell


def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
