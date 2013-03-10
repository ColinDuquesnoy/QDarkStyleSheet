#!/usr/bin/env python
"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.


Requirements:
    - Python 2 or Python 3
    - PySide

.. note.. :: qdarkstyle does not have to be installed to run 
	     the example

"""
# standard imports
import os
import sys

# PySide imports
from PySide import QtGui

# dark style import:
# make the example runnable without install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
import qdarkstyle

# our ui made in QtDesigner
import example_ui


def main():
    """
    Application entry point
    """	
    # create the application and the main window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    
    # setup ui
    ui = example_ui.Ui_MainWindow()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle example")

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))

    # run
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

