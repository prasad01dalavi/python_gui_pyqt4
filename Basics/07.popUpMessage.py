import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))    
        self.button_setting()

    def button_setting(self):
        btn = QtGui.QPushButton("Button Name", self)
        btn.clicked.connect(self.button_message)
        # Call the button_message method when click on button
        btn.resize(70, 30)
        btn.move(210, 150)   # Button position (from left, from up)
        
        self.show()

    def button_message(self):
        choice = QtGui.QMessageBox.question(self, 'Title of The Window',
                                            'Do you want to execute pop up ?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        # Can be Yes, No, Ok

        if choice == QtGui.QMessageBox.Yes:
            print "Button is pressed"
            print 'PoP Up is executed !'
        else:
            print 'PoP Up is Cancelled !'

           
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
