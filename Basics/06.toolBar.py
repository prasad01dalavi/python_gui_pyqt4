import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))    

        self.toolbar_setting()

    def toolbar_setting(self):
        extract_action = QtGui.QAction(QtGui.QIcon('tools.jpg'), 'Tool Info',
                                      self)
        # I can place icon for tool or leave the parameter
        extract_action.triggered.connect(self.tool_message)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extract_action)
        self.show()
        
    def tool_message(self):
        print 'Tool is selected'

           
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
