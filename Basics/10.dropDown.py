import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))

        self.drop_down_menu()
        self.show()

    def drop_down_menu(self):
        combo_box = QtGui.QComboBox(self)
        combo_box.addItem('Choice 1')
        combo_box.addItem('Choice 2')
        combo_box.addItem('Choice 3')
        combo_box.addItem('Choice 4')
        combo_box.addItem('Choice 5')

        combo_box.move(50, 250)
        combo_box.activated[str].connect(self.choice_action)

    def choice_action(self, text):
        print 'Selected Choice =', text

           
def run_app():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run_app()
