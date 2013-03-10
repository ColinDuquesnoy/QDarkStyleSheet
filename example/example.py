#!/usr/bin/env python
import os
from os.path import abspath, dirname

import sys
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/../..'))

from PySide import QtGui
import QDarkStyleSheet
import example_ui



# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup ui
ui = example_ui.Ui_MainWindow()
ui.setupUi(window)

# setup stylesheet
app.setStyleSheet(QDarkStyleSheet.load_stylesheet(pyside=True))

# run
window.show()
app.exec_()
