import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('My Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        
        print 'Welcome to My First Python App !'
        
        self.menubar_setting()
        self.show()

    def menubar_setting(self):
        extract_action = QtGui.QAction('&Close the window', self)
        extract_action.setShortcut('Ctrl+Q')
        extract_action.setStatusTip('Window will be closed.')
        extract_action.triggered.connect(QtCore.QCoreApplication.instance().
                                         quit)
        self.statusBar()
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)

        # File Opening
        open_file = QtGui.QAction('&Open File', self)
        open_file.setShortcut('Ctrl+o')
        open_file.setStatusTip('Open File')
        open_file.triggered.connect(self.file_open)

        file_menu.addAction(open_file)
        # Add file opening action to menu
        # ------------------------------------------------------------------- #

        # Saving Files
        save_file = QtGui.QAction('&Save File',self)
        save_file.setShortcut('Ctrl+s')
        save_file.setStatusTip('Saves File')
        save_file.triggered.connect(self.file_save)
        # Call the file_save function to save the file

        file_menu.addAction(save_file)
        # ------------------------------------------------------------------- #

        # Editor
        open_editor = QtGui.QAction('&Editor',self)
        open_editor.setShortcut('Ctrl+E')
        open_editor.setStatusTip('Open Editor')
        open_editor.triggered.connect(self.editor)
        
        editorMenu = main_menu.addMenu('&Edit')
        editorMenu.addAction(open_editor)

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')   # Read the opened file

        self.editor()   # open the file in editor

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'save File')
        my_file = open(name, 'w')
        text = self.textEdit.toPlainText()
        my_file.write(text)
        my_file.close()
        
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
