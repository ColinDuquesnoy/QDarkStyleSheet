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

    python example.py  --qt_from=pyqt5 --no_dark

.. note.. :: qdarkstyle does not have to be installed to run the example.

"""

# Standard library imports
import qdarkstyle
import argparse
import logging
import os
import sys
import platform
import time

# Third part libraries
import helpdev

# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

# set log for debug
logging.basicConfig(level=logging.DEBUG)

# must be in this place, after setting path, to not need to install

# Constants
SCREENSHOTS_PATH = qdarkstyle.IMAGES_PATH


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qt_from', default='qtpy',
                        choices=['pyqt', 'pyqt5', 'pyside', 'pyside2', 'qtpy', 'pyqtgraph', 'qt.py'],
                        help="Choose which wrapper/framework is to be used to run the example.", type=str)
    parser.add_argument('--no_dark', action='store_true',
                        help="Exihibts the original  window (without qdarkstyle).")
    parser.add_argument('--test', action='store_true',
                        help="Auto close window after 2s.")
    parser.add_argument('--reset', action='store_true',
                        help="Reset GUI settings (position, size).")
    parser.add_argument('--screenshots', action='store_true',
                        help="Generate screenshots.")

    # Parsing arguments from command line
    args = parser.parse_args()

    # To avoid problems when testing without screen
    if args.test:
        os.environ['QT_QPA_PLATFORM'] = 'offscreen'

    # Set QT_API variable before importing QtPy
    if args.qt_from in ['pyqt', 'pyqt5', 'pyside', 'pyside2']:
        os.environ['QT_API'] = args.qt_from
    elif args.qt_from == 'pyqtgraph':
        os.environ['QT_API'] = os.environ['PYQTGRAPH_QT_LIB']
    elif args.qt_from in ['qt.py', 'qt']:
        try:
            import Qt
        except ImportError:
            print('Could not import Qt (Qt.Py)')
        else:
            os.environ['QT_API'] = Qt.__binding__

    # QtPy imports
    from qtpy import API_NAME, QT_VERSION, PYQT_VERSION, PYSIDE_VERSION
    from qtpy import __version__ as QTPY_VERSION
    from qtpy.QtWidgets import QApplication, QMainWindow, QDockWidget, QStatusBar, QLabel, QPushButton
    from qtpy.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize

    # Set API_VERSION variable
    API_VERSION = ''

    if PYQT_VERSION:
        API_VERSION = PYQT_VERSION
    elif PYSIDE_VERSION:
        API_VERSION = PYSIDE_VERSION
    else:
        API_VERSION = 'Not found'

    # Import examples UI according to wrapper
    from ui.mw_menus_ui import Ui_MainWindow as ui_main

    from ui.dw_buttons_ui import Ui_DockWidget as ui_buttons
    from ui.dw_displays_ui import Ui_DockWidget as ui_displays
    from ui.dw_inputs_fields_ui import Ui_DockWidget as ui_inputs_fields
    from ui.dw_inputs_no_fields_ui import Ui_DockWidget as ui_inputs_no_fields

    from ui.dw_widgets_ui import Ui_DockWidget as ui_widgets
    from ui.dw_views_ui import Ui_DockWidget as ui_views
    from ui.dw_containers_tabs_ui import Ui_DockWidget as ui_containers_tabs
    from ui.dw_containers_no_tabs_ui import Ui_DockWidget as ui_containers_no_tabs

    def write_settings(window):
        """Get window settings and write it into a file."""
        settings = QSettings('QDarkStyle', 'QDarkStyle Example')
        settings.setValue('pos', window.pos())
        settings.setValue('size', window.size())
        settings.setValue('state', window.saveState())

    def read_settings(window, reset=False):
        """Read and set window settings from a file."""
        settings = QSettings('QDarkStyle', 'QDarkStyle Example')

        try:
            pos = settings.value('pos', window.pos())
            size = settings.value('size', window.size())
            state = settings.value('state', window.saveState())
        except Exception:
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

    style = ''

    if not args.no_dark:
        style = qdarkstyle.load_stylesheet()

    app.setStyleSheet(style)

    # create main window
    window = QMainWindow()
    window.setObjectName('mainwindow')

    ui = ui_main()
    ui.setupUi(window)

    title = ("QDarkStyle Example - " +
             "(QDarkStyle=v" + qdarkstyle.__version__ +
             ", QtPy=v" + QTPY_VERSION +
             ", " + API_NAME + "=v" + API_VERSION +
             ", Qt=v" + QT_VERSION +
             ", Python=v" + platform.python_version() + ")")

    window.setWindowTitle(title)

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

    # issues #9120, #9121 on Spyder
    qstatusbar = QStatusBar()
    qstatusbar.addWidget(QLabel('Issue Spyder #9120, #9121 - background not matching.'))
    qstatusbar.addWidget(QPushButton('OK'))
    qstatusbar.addWidget(QLabel('INFO: ' + title))
    window.setStatusBar(qstatusbar)

    # Todo: add report info and other info in HELP graphical

    # auto quit after 2s when testing on travis-ci
    if args.test:
        QTimer.singleShot(2000, app.exit)

    if not args.screenshots:
        # do not read when taking screenshots
        read_settings(window, args.reset)
        window.showMaximized()

    # Save screenshots for differents displays and quit
    if args.screenshots:
        create_screenshots(app, window, args.no_dark)

    app.exec_()
    write_settings(window)


def create_screenshots(app, window, no_dark):
    """Save screenshots for different application views and quit."""
    from qtpy.QtCore import QCoreApplication, QTimer, Qt
    from qtpy.QtGui import QGuiApplication
    from qtpy.QtWidgets import QDockWidget, QTabWidget

    theme = 'no_dark' if no_dark else 'dark'
    print('\nCreating {} screenshots'.format(theme))

    docks = window.findChildren(QDockWidget)
    tabs = window.findChildren(QTabWidget)

    widget_data = {
        'containers_no_tabs_buttons.png': [
            'Containers - No Tabs',
            'Buttons',
        ],
        'containers_tabs_displays.png': [
            'Containers - Tabs',
            'Displays',
        ],
        'widgets_inputs_fields.png': [
            'Widgets',
            'Inputs - Fields',
        ],
        'views_inputs_no_fields.png': [
            'Views',
            'Inputs - No Fields',
        ]
    }

    # Central widget tabs of with examples
    tab = [tab for tab in tabs if tab.count() >= 12][0]
    tab.setCurrentIndex(0)

    QCoreApplication.processEvents()

    for fname_suffix, dw_titles in widget_data.items():

        png_path = os.path.join(SCREENSHOTS_PATH, theme + '_' + fname_suffix)
        print('\t' + png_path)

        dw_list = []

        for dw in docks:
            if dw.windowTitle() in dw_titles:
                print('Evidencing : ', dw.windowTitle())
                dw_list.append(dw)
                dw.raise_()
                dw.show()
                QCoreApplication.processEvents()

        # Attention: any change in update, processEvent and sleep calls
        # make those screenshots not working, specially the first one.
        # It seems that processEvents are not working properly

        window.update()
        window.showFullScreen()
        QCoreApplication.processEvents()

        time.sleep(0.5)
        QCoreApplication.processEvents()

        screen = QGuiApplication.primaryScreen()
        QCoreApplication.processEvents()
        pixmap = screen.grabWindow(window.winId())

        # Yeah, this is duplicated to avoid screenshot problems
        screen = QGuiApplication.primaryScreen()
        QCoreApplication.processEvents()
        pixmap = screen.grabWindow(window.winId())

        img = pixmap.toImage()
        img.save(png_path)

        QCoreApplication.processEvents()

    QCoreApplication.processEvents()
    window.close()
    print('\n')
    app.exit(sys.exit())


if __name__ == "__main__":
    sys.exit(main())
