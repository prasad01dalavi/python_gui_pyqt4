import sys                      
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):             # Making a class Window
    def __init__(self):                      # Constructor
        super(Window, self).__init__()       # Feature of Inheritance
        self.setGeometry(50, 50, 500, 300)
        # Size of the window (50px from left, 500px from up, width, height)

        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))  # Image path for Icon
        self.show()


app = QtGui.QApplication([])    # Creates window app
# Create an object to execute constructor in class Window
GUI = Window()                  # GUI is an object/instance of a class Window
sys.exit(app.exec_())           # makes my app stable and responding
