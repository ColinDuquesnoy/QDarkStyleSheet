import sys
from PySide import QtGui
import example_ui

# import the style resources
import style_pyside_rc


# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup ui
ui = example_ui.Ui_MainWindow()
ui.setupUi(window)

# setup stylesheet
with open("style.qss", 'r') as stylesheet:
    app.setStyleSheet(stylesheet.read())

# run
window.show()
app.exec_()
