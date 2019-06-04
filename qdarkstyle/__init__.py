#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""QDarkStyle is a dark stylesheet for Python and Qt applications.

This module provides a function to transparently load the stylesheets
with the correct rc file.

First, start importing our module

.. code-block:: python

    import qdarkstyle

Then you can get stylesheet provided by QDarkStyle for various Qt wrappers
as shown bellow

.. code-block:: python

    # PySide
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside()
    # PySide 2
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()
    # PyQt4
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt()
    # PyQt5
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()

Or from environment variables provided for QtPy or PyQtGraph, see

.. code-block:: python

    # QtPy
    dark_stylesheet = qdarkstyle.load_stylesheet_from_environment()
    # PyQtGraph
    dark_stylesheet = qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph)

Finally, set your QApplication with it

.. code-block:: python

    app.setStyleSheet(dark_stylesheet)

Enjoy!

"""

# Standard library imports
import logging
import os
import platform
import warnings

# Local imports
from qdarkstyle.palette import DarkPalette

__version__ = "2.8"

_logger = logging.getLogger(__name__)

# Constants
QDARK_QT_BINDING = ''
"""str: Qt binding in use."""

# Folder's path
REPO_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

EXAMPLE_PATH = os.path.join(REPO_PATH, 'example')
IMAGES_PATH = os.path.join(REPO_PATH, 'images')
PACKAGE_PATH = os.path.join(REPO_PATH, 'qdarkstyle')

QSS_PATH = os.path.join(PACKAGE_PATH, 'qss')
RC_PATH = os.path.join(PACKAGE_PATH, 'rc')
SVG_PATH = os.path.join(PACKAGE_PATH, 'svg')

# File names
QSS_FILE = 'style.qss'
QRC_FILE = QSS_FILE.replace('.qss', '.qrc')

MAIN_SCSS_FILE = 'main.scss'
STYLES_SCSS_FILE = '_styles.scss'
VARIABLES_SCSS_FILE = '_variables.scss'

# File paths
QSS_FILEPATH = os.path.join(PACKAGE_PATH, QSS_FILE)
QRC_FILEPATH = os.path.join(PACKAGE_PATH, QRC_FILE)

MAIN_SCSS_FILEPATH = os.path.join(QSS_PATH, MAIN_SCSS_FILE)
STYLES_SCSS_FILEPATH = os.path.join(QSS_PATH, STYLES_SCSS_FILE)
VARIABLES_SCSS_FILEPATH = os.path.join(QSS_PATH, VARIABLES_SCSS_FILE)

DEPRECATION_MSG = '''This function is deprecated in {},
and it will be removed in v3.0. Please, set the
wanted binding by using QtPy environment variable QT_API,
then use load_stylesheet() or use load_stylesheet()
passing the argument qt_api= 'wanted_binding'.'''.format(__version__)


def _apply_os_patches(stylesheet, QFile, QTextStream):
    """
    Apply OS-only specific stylesheet pacthes.

    Args:
        stylesheet(str): current stylesheet to apply patches.

    Returns:
        str: stylesheet string (css).
    """
    os_fix = ""

    if platform.system().lower() == 'darwin':
        # See issue #12
        os_fix = '''
        QDockWidget::title
        {{
            background-color: {color};
            text-align: center;
            height: 12px;
        }}
        '''.format(color=DarkPalette.COLOR_BACKGROUND_NORMAL)

    # Only open the QSS file if any patch is needed
    #if os_fix:

    _logger.info("Found OS patches to be applyed.")
    qss_file = QFile(QSS_FILEPATH)

    if not qss_file.exists():
        stylesheet = ""
        _logger.error("Unable to load qss file, file not found in "
                        "resources. OS patch not applied.")
    else:
        qss_file.open(QFile.ReadOnly | QFile.Text)
        text_stream = QTextStream(qss_file)
        stylesheet = text_stream.readAll()
        stylesheet += os_fix
        _logger.info("OS patches applyed successfuly.")

    return stylesheet


def _apply_binding_patches(stylesheet):
    """
    Apply binding-only specific stylesheet patches for the same OS.

    Args:
        stylesheet(str): current stylesheet to apply patches.

    Returns:
        str: stylesheet string (css).
    """
    binding_fix = ""

    if binding_fix:
        _logger.info("Found binding patches to be applyed.")

    return stylesheet


def _apply_version_patches(stylesheet):
    """
    Apply version-only specific stylesheet patches for the same binding.

    Args:
        stylesheet(str): current stylesheet to apply patches.

    Returns:
        str: stylesheet string (css).
    """
    version_fix = ""

    if version_fix:
        _logger.info("Found version patches to be applyed.")

    return stylesheet


def _apply_application_patches(QCoreApplication, QPalette, QColor):
    """
    Apply application level fixes on the QPalette.
    """
    # See issue #139
    color = DarkPalette.COLOR_SELECTION_LIGHT
    qcolor = QColor(color)
    app = QCoreApplication.instance()

    if app:
        palette = app.palette()
        palette.setColor(QPalette.Normal, QPalette.Link, qcolor)
        app.setPalette(palette)
        _logger.info("Application patches applyed successfuly.")


def _load_stylesheet(qt_api=''):
    """
    Load the stylesheet based on QtPy abstraction layer environment variable.

    If the argument is not passed, it will use the current QT_API environment
    variable to make the imports of Qt bindings. If passed, it will set this
    variable then make the imports.

    Args:
        qt_api (str): qt binding name to set QT_API environment variable.
                      Default is ''. Possible values are pyside, pyside2
                      pyqt4, pyqt5. Not case sensitive.

    Note:
        - Note that the variable QT_API is read when first imported. So,
          pay attention to importing order.
        - If you are using other abstraction layer, i.e PyQtGraph to do
          imports on Qt things you must set both to use the same Qt
          binding (PyQt, PySide).
        - OS, Binding and binding version number, and application specific
          patches are applyed in this order.

    Returns:
        str: stylesheet string (css).
    """

    if qt_api:
        os.environ['QT_API'] = qt_api

    # Import is made after setting QT_API
    from qtpy.QtCore import QCoreApplication, QFile, QTextStream
    from qtpy.QtGui import QColor, QPalette

    # Todo: check execution order for these functions
    # 1. Apply OS specific patches
    stylesheet = _apply_os_patches("", QFile, QTextStream)

    # 2. Apply binding specific patches
    stylesheet = _apply_binding_patches(stylesheet)

    # 3. Apply binding version specific patches
    stylesheet = _apply_version_patches(stylesheet)

    # 4. Apply palette fix. See issue #139
    _apply_application_patches(QCoreApplication, QPalette, QColor)

    if stylesheet:
        return stylesheet
    else:
        # Todo: Should import compiled style_rc file here? Or before?
        import qdarkstyle.style_rc


def load_stylesheet_from_environment(is_pyqtgraph=False):
    """
    Load the stylesheet from QT_API (or PYQTGRAPH_QT_LIB) environment variable.

    Args:
        is_pyqtgraph (bool): True if it is to be set using PYQTGRAPH_QT_LIB.

    Raises:
        KeyError: if PYQTGRAPH_QT_LIB does not exist.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)

    if is_pyqtgraph:
        stylesheet = _load_stylesheet(qt_api=os.environ('PYQTGRAPH_QT_LIB'))
    else:
        stylesheet = _load_stylesheet()

    return stylesheet


def load_stylesheet(pyside=True):
    """
    Load the stylesheet. Takes care of importing the rc module.

    Args:
        pyside (bool): True to load the Pyside rc file, False to load
                       the PyQt rc file.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)

    stylesheet = ""

    if pyside:
        stylesheet = _load_stylesheet(qt_api='pyside')
        if not stylesheet:
            stylesheet = _load_stylesheet(qt_api='pyside2')
    else:
        stylesheet = _load_stylesheet(qt_api='pyqt4')
        if not stylesheet:
            stylesheet = _load_stylesheet(qt_api='pyqt5')

    return stylesheet


def load_stylesheet_pyside():
    """
    Load the stylesheet for use in a PySide application.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)
    return _load_stylesheet(qt_api='pyside')


def load_stylesheet_pyside2():
    """
    Load the stylesheet for use in a PySide2 application.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)
    return _load_stylesheet(qt_api='pyside2')


def load_stylesheet_pyqt():
    """
    Load the stylesheet for use in a PyQt4 application.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)
    return _load_stylesheet(qt_api='pyqt4')


def load_stylesheet_pyqt5():
    """
    Load the stylesheet for use in a PyQt5 application.

    Returns:
        str: the stylesheet string.
    """
    warnings.warn(DEPRECATION_MSG, DeprecationWarning)
    return _load_stylesheet(qt_api='pyqt5')
