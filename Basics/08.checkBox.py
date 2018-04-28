import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.checkbox_setting()
        self.show()

    def checkbox_setting(self):
        checkbox = QtGui.QCheckBox('Enlarge Window', self)
        checkbox.move(100,25)
        checkbox.stateChanged.connect(self.enlarge_window)
        # if window is ticked then go to enlarge function
        
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            print 'Check Box is ticked.'
            self.setGeometry(50, 50, 1000, 600)
        else:
            print 'Check Box is unticked.'
            self.setGeometry(50, 50, 500, 300)

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
