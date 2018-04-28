import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))    

        extract_action = QtGui.QAction('&Close the window', self)
        extract_action.setShortcut('Ctrl+Q')  # short cut to do the same thing
        extract_action.setStatusTip('Window will be closed.')
        # Working tip for the menu option
        extract_action.triggered.connect(QtCore.QCoreApplication.instance().
                                         quit)
        # When the option is selected(clicked) do this
        self.statusBar()  # Builds status bar

        main_menu = self.menuBar()
        file_menu1 = main_menu.addMenu('&File')
        file_menu2 = main_menu.addMenu('&Edit')
        file_menu3 = main_menu.addMenu('&Format')
        file_menu4 = main_menu.addMenu('&Run')

        file_menu1.addAction(extract_action)  # Adding action for first menu
        # Provides the option for menu1 i.e. declared as File
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
