import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('My Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.menubar_setting()
        self.show()
                                    
    def menubar_setting(self):
        extract_action = QtGui.QAction('&Close the window',self)
        extract_action.setShortcut('Ctrl+Q')
        extract_action.setStatusTip('Window will be closed.')
        extract_action.triggered.connect(QtCore.QCoreApplication.instance().
                                         quit)
        self.statusBar()
        main_menu = self.menuBar()
        
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)
        # ------------------------------------------------------------------- #

        # File Opening
        open_file = QtGui.QAction('&Open File',self)
        open_file.setShortcut('Ctrl+o')
        open_file.setStatusTip('Open File')
        open_file.triggered.connect(self.file_open)

        file_menu.addAction(open_file)
        # Add file opening action to menu
        # ------------------------------------------------------------------- #

        # Now, open the file in Editor
        open_editor = QtGui.QAction('&Editor',self)
        open_editor.setShortcut('Ctrl+E')
        open_editor.setStatusTip('Open Editor')
        open_editor.triggered.connect(self.editor)
        # When Editor is selected, just open simple blank editor

        editor_menu = main_menu.addMenu('&Edit')
        # Add editor menu to menu bar
        editor_menu.addAction(open_editor)

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        # title open file
        file = open(name, 'r')  # Open the file in read mode
        self.editor()           # Call the editor function to show that file

        with file:
            text = file.read()   # Read the opened file and save in text
            self.textEdit.setText(text)

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)


def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
