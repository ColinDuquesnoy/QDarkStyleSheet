#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example of qdarkstyle use for Python and Qt applications.

This module a main window with every item that could be created with
Qt Design (common ones) in the basic states (enabled/disabled), and
(checked/unchecked) for those who has this attribute.

Requirements:

    - Python 2 or Python 3
    - PyQt4 or PyQt5 or PySide
    - QtPy or PyQtGraph (if choosen)

To run this example using PyQt4, simple do

.. code-block:: python

    python example.py

or

.. code-block:: python

    python example.py  --qt_from=pyqt

Other options for qt_from are: pyqt5, pyside, qtpy and pyqtgraph.

You also can run the example without dark theme (no_dark), to check for
problems.

.. code-block:: python

    python example.py  --qt_from=pyqt --no_dark

.. note.. :: qdarkstyle does not have to be installed to run the example.

"""

import logging
import sys
import argparse

# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

import qdarkstyle


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qt_from', default='pyqt',
                        choices=['pyqt', 'pyqt5', 'pyside', 'qtpy', 'pyqtgraph'],
                        help="Choose which wrapper/framework is to be used to run the example.", type=str)
    parser.add_argument('--no_dark', action='store_true',
                        help="Exihibts the original  window (without qdarkstyle).")

    # parsing arguments from command line
    args = parser.parse_args()

    # set log for debug
    logging.basicConfig(level=logging.DEBUG)

    if args.qt_from == 'pyside':
        # using PySide wrapper
        from PySide.QtGui import QApplication, QMainWindow, QDockWidget
        from PySide.QtCore import QTimer, Qt
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_pyside_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_pyside_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyside_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyside_ui import Ui_DockWidget as ui_inputs
        from ui.dw_inputs_no_fields_pyside_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_pyside()

    elif args.qt_from == 'pyqt':
        # using PyQt4 wrapper
        from PyQt4.QtGui import QApplication, QMainWindow, QDockWidget
        from PyQt4.QtCore import QTimer, Qt
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_pyqt_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_pyqt_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqt_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqt_ui import Ui_DockWidget as ui_inputs
        from ui.dw_inputs_no_fields_pyqt_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_pyqt()

    elif args.qt_from == 'pyqt5':
        # using PyQt5 wrapper
        from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
        from PyQt5.QtCore import QTimer, Qt
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_pyqt5_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_pyqt5_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqt5_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqt5_ui import Ui_DockWidget as ui_inputs
        from ui.dw_inputs_no_fields_pyqt5_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_pyqt5()

    elif args.qt_from == 'qtpy':
        # using QtPy API
        from qtpy.QtWidgets import QApplication, QMainWindow, QDockWidget
        from qtpy.QtCore import QTimer, Qt
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_qtpy_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_qtpy_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_qtpy_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_qtpy_ui import Ui_DockWidget as ui_inputs
        from ui.dw_inputs_no_fields_qtpy_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_from_environment()

    elif args.qt_from == 'pyqtgraph':
        # using PyQtGraph API
        from pyqtgraph.Qt import QtGui, QtCore
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_pyqtgraph_ui import Ui_MainWindow as ui_main
        from ui.mw_dw_buttons_pyqtgraph_ui import Ui_DockWidget as ui_buttons
        from ui.mw_dw_displays_pyqtgraph_ui import Ui_DockWidget as ui_displays
        from ui.mw_dw_inputs_fields_pyqtgraph_ui import Ui_DockWidget as ui_inputs
        from ui.mw_dw_inputs_no_fields_pyqtgraph_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True)

    if args.no_dark:
        style = ''

    # create the application
    app = QApplication(sys.argv)

    # setup stylesheet
    app.setStyleSheet(style)

    # create main window
    window = QMainWindow()
    ui = ui_main()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle v." + qdarkstyle.__version__ +
                          " - Example - Using " + args.qt_from)

    # create docks for buttons
    dw_buttons = QDockWidget()
    ui_buttons = ui_buttons()
    ui_buttons.setupUi(dw_buttons)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_buttons)

    # create docks for buttons
    dw_displays = QDockWidget()
    ui_displays = ui_displays()
    ui_displays.setupUi(dw_displays)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_displays)

    # create docks for inputs - fields
    dw_inputs = QDockWidget()
    ui_inputs = ui_inputs()
    ui_inputs.setupUi(dw_inputs)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs)

    # create docks for inputs - no fields
    dw_inputs_no_field = QDockWidget()
    ui_inputs_no_field = ui_inputs_no_fields()
    ui_inputs_no_field.setupUi(dw_inputs_no_field)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_no_field)

    # tabify docks
    window.tabifyDockWidget(dw_buttons, dw_displays)
    window.tabifyDockWidget(dw_displays, dw_inputs)
    window.tabifyDockWidget(dw_inputs, dw_inputs_no_field)

    # connect some actions, signals and functions
    # auto quit after 2s when testing on travis-ci

    if "--travis" in sys.argv:
        QTimer.singleShot(2000, app.exit)

    # run
    window.showMaximized()
    app.exec_()

if __name__ == "__main__":
    sys.exit(main())
