import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('My Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.menubar_setting()

        self.show()

    def menubar_setting(self):
        extract_action = QtGui.QAction('&Close the window', self)
        extract_action.setShortcut('Ctrl+Q')
        extract_action.setStatusTip('Window will be closed.')
        extract_action.triggered.connect(QtCore.QCoreApplication.instance().
                                         quit)

        self.statusBar()   # Place the menu on status bar
        main_menu = self.menuBar()
        
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)
        # Provides the option for menu1 i.e. declared as File

        # Editor Settings
        open_editor = QtGui.QAction('&Editor', self)
        open_editor.setShortcut('Ctrl+E')
        open_editor.setStatusTip('Open Editor')
        open_editor.triggered.connect(self.editor)

        editor_menu = main_menu.addMenu('&Edit')  # Adds editor to menu bar
        editor_menu.addAction(open_editor)
        # When click on Edit, perform the action as specified by open_editor

    def editor(self):  # This is function that actually gives the editor window
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)


def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
