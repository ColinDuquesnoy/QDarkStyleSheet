#!python
# -*- coding: utf-8 -*-

"""Example of qdarkstyle use for Python and Qt applications.

This module a main window with every item that could be created with
Qt Design (common ones) in the basic states (enabled/disabled), and
(checked/unchecked) for those who has this attribute.

Requirements:

    - Python 2 or Python 3
    - PyQt4 or PyQt5 or PySide or PySide2
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
import os

# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

# must be in this place, after setting path, to not need to install
import qdarkstyle
from qdarkstyle import QT_BINDING, QT_ABSTRACTION


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qt_from', default='qtpy',
                        choices=['pyqt', 'pyqt5', 'pyside','pyside2', 'qtpy', 'pyqtgraph'],
                        help="Choose which wrapper/framework is to be used to run the example.", type=str)
    parser.add_argument('--no_dark', action='store_true',
                        help="Exihibts the original  window (without qdarkstyle).")
    parser.add_argument('--test', action='store_true',
                        help="Auto close window after 2s.")
    parser.add_argument('--reset', action='store_true',
                        help="Reset GUI settings (position, size).")
    # parsing arguments from command line
    args = parser.parse_args()

    # set log for debug
    logging.basicConfig(level=logging.DEBUG)

    # to avoid problems when testing without screen
    if args.test:
        os.environ['QT_QPA_PLATFORM']='offscreen'

    if args.qt_from == 'pyside':
        # using PySide wrapper
        from PySide.QtGui import QApplication, QMainWindow, QDockWidget
        from PySide.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        # import examples UI according to wrapper
        from ui.mw_menus_pyside_ui import Ui_MainWindow as ui_main

        from ui.dw_buttons_pyside_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyside_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyside_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_pyside_ui import Ui_DockWidget as ui_inputs_no_fields

        from ui.dw_widgets_pyside_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_pyside_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_pyside_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_pyside_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_pyside()

    elif args.qt_from == 'pyqt':
        # using PyQt4 wrapper
        from PyQt4.QtGui import QApplication, QMainWindow, QDockWidget
        from PyQt4.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        # import examples UI according to wrapper
        from ui.mw_menus_pyqt_ui import Ui_MainWindow as ui_main

        from ui.dw_buttons_pyqt_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqt_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqt_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_pyqt_ui import Ui_DockWidget as ui_inputs_no_fields

        from ui.dw_widgets_pyqt_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_pyqt_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_pyqt_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_pyqt_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_pyqt()

    elif args.qt_from == 'pyqt5':
        # using PyQt5 wrapper
        from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
        from PyQt5.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        # import examples UI according to wrapper
        from ui.mw_menus_pyqt5_ui import Ui_MainWindow as ui_main

        from ui.dw_buttons_pyqt5_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqt5_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqt5_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_pyqt5_ui import Ui_DockWidget as ui_inputs_no_fields

        from ui.dw_widgets_pyqt5_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_pyqt5_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_pyqt5_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_pyqt5_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_pyqt5()

    elif args.qt_from == 'pyside2':
        # using PyQt5 wrapper
        from PySide2.QtWidgets import QApplication, QMainWindow, QDockWidget
        from PySide2.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        # import examples UI according to wrapper
        from ui.mw_menus_pyside2_ui import Ui_MainWindow as ui_main

        from ui.dw_buttons_pyside2_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyside2_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyside2_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_pyside2_ui import Ui_DockWidget as ui_inputs_no_fields

        from ui.dw_widgets_pyside2_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_pyside2_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_pyside2_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_pyside2_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_pyside2()

    elif args.qt_from == 'qtpy':
        # using QtPy API
        from qtpy.QtWidgets import QApplication, QMainWindow, QDockWidget
        from qtpy.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        # import examples UI according to wrapper
        from ui.mw_menus_qtpy_ui import Ui_MainWindow as ui_main

        from ui.dw_buttons_qtpy_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_qtpy_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_qtpy_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_qtpy_ui import Ui_DockWidget as ui_inputs_no_fields

        from ui.dw_widgets_qtpy_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_qtpy_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_qtpy_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_qtpy_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_from_environment()

    elif args.qt_from == 'pyqtgraph':
        # using PyQtGraph API
        from pyqtgraph.Qt.QtGui import QApplication, QMainWindow, QDockWidget
        from pyqtgraph.Qt.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize
        #from pyqtgraph.Qt import QtGui, QtCore
        # import examples UI according to wrapper
        from ui.mw_menus_pyqtgraph_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_pyqtgraph_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqtgraph_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqtgraph_ui import Ui_DockWidget as ui_inputs_fields
        from ui.dw_inputs_no_fields_pyqtgraph_ui import Ui_DockWidget as ui_inputs_no_fields
        from ui.dw_widgets_pyqtgraph_ui import Ui_DockWidget as ui_widgets
        from ui.dw_views_pyqtgraph_ui import Ui_DockWidget as ui_views
        from ui.dw_containers_tabs_pyqtgraph_ui import Ui_DockWidget as ui_containers_tabs
        from ui.dw_containers_no_tabs_pyqtgraph_ui import Ui_DockWidget as ui_containers_no_tabs
        # getting style
        style = qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True)

    if args.no_dark:
        style = ''

    def write_settings(window):
        """Get window settings and write it into a file."""
        settings = QSettings('QDarkStyle', 'QDarkStyle Example')
        settings.setValue('pos', window.pos())
        settings.setValue('size', window.size())
        settings.setValue('state', window.saveState())

    def read_settings(window, reset=False):
        """Read and set window settings from a file."""
        settings = QSettings('QDarkStyle', 'QDarkStyle Example')
        if args.qt_from == 'pyside' or args.qt_from == 'pyside2':
            pos = settings.value('pos', window.pos())
            size = settings.value('size', window.size())
            state = settings.value('state', window.saveState())
        else:
            pos = settings.value('pos', window.pos(), type='QPoint')
            size = settings.value('size', window.size(), type='QSize')
            state = settings.value('state', window.saveState(), type='QByteArray')

        if not reset:
            window.restoreState(state)
            window.resize(size)
            window.move(pos)




    # create the application
    app = QApplication(sys.argv)
    app.setOrganizationName('QDarkStyle')
    app.setApplicationName('QDarkStyle Example')

    # setup stylesheet
    app.setStyleSheet(style)

    # create main window
    window = QMainWindow()
    window.setObjectName('mainwindow')
    ui = ui_main()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle v." + qdarkstyle.__version__)

    # create docks for buttons
    dw_buttons = QDockWidget()
    dw_buttons.setObjectName('buttons')
    ui_buttons = ui_buttons()
    ui_buttons.setupUi(dw_buttons)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_buttons)

    # create docks for buttons
    dw_displays = QDockWidget()
    dw_displays.setObjectName('displays')
    ui_displays = ui_displays()
    ui_displays.setupUi(dw_displays)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_displays)

    # create docks for inputs - no fields
    dw_inputs_no_fields = QDockWidget()
    dw_inputs_no_fields.setObjectName('inputs_no_fields')
    ui_inputs_no_fields = ui_inputs_no_fields()
    ui_inputs_no_fields.setupUi(dw_inputs_no_fields)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_no_fields)

    # create docks for inputs - fields
    dw_inputs_fields = QDockWidget()
    dw_inputs_fields.setObjectName('_fields')
    ui_inputs_fields = ui_inputs_fields()
    ui_inputs_fields.setupUi(dw_inputs_fields)
    window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_fields)

    # create docks for widgets
    dw_widgets = QDockWidget()
    dw_widgets.setObjectName('widgets')
    ui_widgets = ui_widgets()
    ui_widgets.setupUi(dw_widgets)
    window.addDockWidget(Qt.LeftDockWidgetArea, dw_widgets)

    # create docks for views
    dw_views = QDockWidget()
    dw_views.setObjectName('views')
    ui_views = ui_views()
    ui_views.setupUi(dw_views)
    window.addDockWidget(Qt.LeftDockWidgetArea, dw_views)

    # create docks for containers - no tabs
    dw_containers_no_tabs = QDockWidget()
    dw_containers_no_tabs.setObjectName('containers_no_tabs')
    ui_containers_no_tabs = ui_containers_no_tabs()
    ui_containers_no_tabs.setupUi(dw_containers_no_tabs)
    window.addDockWidget(Qt.LeftDockWidgetArea, dw_containers_no_tabs)

    # create docks for containters - tabs
    dw_containers_tabs = QDockWidget()
    dw_containers_tabs.setObjectName('containers')
    ui_containers_tabs = ui_containers_tabs()
    ui_containers_tabs.setupUi(dw_containers_tabs)
    window.addDockWidget(Qt.LeftDockWidgetArea, dw_containers_tabs)

    # tabify right docks
    window.tabifyDockWidget(dw_buttons, dw_displays)
    window.tabifyDockWidget(dw_displays, dw_inputs_fields)
    window.tabifyDockWidget(dw_inputs_fields, dw_inputs_no_fields)

    # tabify right docks
    window.tabifyDockWidget(dw_containers_no_tabs, dw_containers_tabs)
    window.tabifyDockWidget(dw_containers_tabs, dw_widgets)
    window.tabifyDockWidget(dw_widgets, dw_views)

    # auto quit after 2s when testing on travis-ci
    if args.test:
        QTimer.singleShot(2000, app.exit)

    # run
    qdarkstyle.information()
    read_settings(window, args.reset)
    window.showMaximized()
    app.exec_()
    write_settings(window)



if __name__ == "__main__":
    sys.exit(main())
