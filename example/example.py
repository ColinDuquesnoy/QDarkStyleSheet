#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QDarkStyle - A dark style sheet for Qt applications
#
# Copyright 2012, 2013 Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.


Requirements:
    - Python 2 or Python 3
    - PySide

.. note.. :: qdarkstyle does not have to be installed to run 
	     the example

"""
import os
import sys
from PySide import QtGui
from os.path import abspath, dirname
# make the example runnable without the need to install
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
import qdarkstyle
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

