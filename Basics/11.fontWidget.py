import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.toolbar_setting()
        self.dropdown_styles()
        self.font_widget()
        
        self.show()
    # ----------------------------------------------------------------------- #

    def toolbar_setting(self):
        self.toolBar = self.addToolBar('Extraction')
    # ----------------------------------------------------------------------- #

    def dropdown_styles(self):
        print 'Current Styles:', self.style().objectName()
        self.styleChoice = QtGui.QLabel('Styles:', self)

        combo_box = QtGui.QComboBox(self)
        combo_box.addItem('motif')
        combo_box.addItem('Windows')
        combo_box.addItem('cde')
        combo_box.addItem('Plastique')
        combo_box.addItem('Cleanlooks')
        combo_box.addItem('windowsvista')

        combo_box.move(50, 250)
        self.styleChoice.move(50, 220)
        combo_box.activated[str].connect(self.style_choice)

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
    # ----------------------------------------------------------------------- #

    def font_widget(self):
        font_choice = QtGui.QAction('Font', self)
        # Name for the font menu is given as Font

        font_choice.triggered.connect(self.font_choice)
        # When click on font; go to font_choice method

        self.toolBar.addAction(font_choice)
        
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
