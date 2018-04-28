import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.tool_bar_setting()
        self.dropdown_styles()
        self.color_picker_widget()
        
        self.show()

    def tool_bar_setting(self):
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

    def color_picker_widget (self):
        color = QtGui.QColor(255, 255, 255)
        # font color set to Black....!!!??? not happy with this
        font_color = QtGui.QAction('Font Background Color', self)
        font_color.triggered.connect(self.color_picker)
        self.toolBar.addAction(font_color)
        # add font_color object to the toolbar

        cal = QtGui.QCalendarWidget(self)
        cal.move(280, 135)           # 280 from left,135 from up
        cal.resize(140, 140)         # base X height

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color:%s}' %
                                       color.name())

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
