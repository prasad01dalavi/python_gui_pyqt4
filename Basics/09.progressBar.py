import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.progressbar_setting()
        self.show()

    def progressbar_setting(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(250, 90, 250, 20)
        # distance from left, up, length of the bar, height of the bar

        self.btn = QtGui.QPushButton('Download', self)  # Button Name
        self.btn.move(250, 120)        # position from left, dist from up
        self.btn.clicked.connect(self.download)

    def download(self):
        self.completed = 0
        print 'Downloading Started...'

        while self.completed < 100:            
            self.completed += 0.00005
            self.progress.setValue(self.completed)
            # I will get percentage of the completed value
        print 'Download Complete !'

        # question, information, warning, critical
        choice = QtGui.QMessageBox.information(self, 'Download Status',
                                               'Download Completed !',
                                               QtGui.QMessageBox.Ok)
        # Can be Yes, No, Ok

        if choice == QtGui.QMessageBox.Ok:            
            print 'Download PoP Up is executed !'   
        else:
            pass

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
