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
import copy
import logging
import os
import platform
import sys
import warnings

# Local imports
from qdarkstyle.palette import DarkPalette

if sys.version_info >= (3, 4):
    import importlib

__version__ = "2.6.8"


# Constants
QT_BINDINGS = ['PyQt4', 'PyQt5', 'PySide', 'PySide2']
"""list: values of all Qt bindings to import."""

QT_ABSTRACTIONS = ['qtpy', 'pyqtgraph', 'Qt']
"""list: values of all Qt abstraction layers to import."""

QT4_IMPORT_API = ['QtCore', 'QtGui']
"""list: which subpackage to import for Qt4 API."""

QT5_IMPORT_API = ['QtCore', 'QtGui', 'QtWidgets']
"""list: which subpackage to import for Qt5 API."""

QT_API_VALUES = ['pyqt', 'pyqt5', 'pyside', 'pyside2']
"""list: values for QT_API environment variable used by QtPy."""

QT_LIB_VALUES = ['PyQt', 'PyQt5', 'PySide', 'PySide2']
"""list: values for PYQTGRAPH_QT_LIB environment variable used by PyQtGraph."""

QT_BINDING = 'Not set or nonexistent'
"""str: Qt binding in use."""

QT_ABSTRACTION = 'Not set or nonexistent'
"""str: Qt abstraction layer in use."""

# File names
VARIABLES_SCSS_FILE = '_variables.scss'
MAIN_SCSS_FILE = 'main.scss'
STYLE_FILE = 'style.qss'
QRC_FILE = STYLE_FILE.replace('.qss', '.qrc')

# Paths
PACKAGE_PATH = os.path.abspath(os.path.dirname(__file__))
REPO_PATH = os.path.dirname(PACKAGE_PATH)
QSS_PATH = os.path.join(PACKAGE_PATH, 'qss')
RC_PATH = os.path.join(PACKAGE_PATH, 'rc')
SVG_PATH = os.path.join(PACKAGE_PATH, 'svg')

# File paths
QSS_FILEPATH = os.path.join(PACKAGE_PATH, STYLE_FILE)
QRC_FILEPATH = os.path.join(PACKAGE_PATH, QRC_FILE)
MAIN_SCSS_FILEPATH = os.path.join(QSS_PATH, MAIN_SCSS_FILE)
VARIABLES_SCSS_FILEPATH = os.path.join(QSS_PATH, VARIABLES_SCSS_FILE)


def _logger():
    return logging.getLogger('qdarkstyle')


def _qt_wrapper_import(qt_api):
    """
    Check if Qt API defined can be imported.

    :param qt_api: Qt API string to test import

    :return load function fot given qt_api, otherwise empty string

    """
    qt_wrapper = ''
    loader = ""

    try:
        if qt_api == 'PyQt' or qt_api == 'pyqt':
            import PyQt4
            qt_wrapper = 'PyQt4'
            loader = load_stylesheet_pyqt()
        elif qt_api == 'PyQt5' or qt_api == 'pyqt5':
            import PyQt5
            qt_wrapper = 'PyQt5'
            loader = load_stylesheet_pyqt5()
        elif qt_api == 'PySide' or qt_api == 'pyside':
            import PySide
            qt_wrapper = 'PySide'
            loader = load_stylesheet_pyside()
        elif qt_api == 'PySide2' or qt_api == 'pyside2':
            import PySide2
            qt_wrapper = 'PySide2'
            loader = load_stylesheet_pyside2()
    except ImportError as err:
        _logger().error("Impossible import Qt wrapper.\n %s", str(err))
    else:
        _logger().info("Using Qt wrapper = %s ", qt_wrapper)
        QT_BINDING = qt_wrapper
    finally:
        return loader


def _apply_stylesheet_patches(stylesheet):
    """Apply OS specific stylesheet pacthes."""
    # See issue #12
    if platform.system().lower() == 'darwin':
        mac_fix = '''
        QDockWidget::title
        {{
            background-color: {color};
            text-align: center;
            height: 12px;
        }}
        '''.format(color=DarkPalette.COLOR_BACKGROUND_NORMAL)
        stylesheet += mac_fix

    return stylesheet


def _apply_palette_fix(QCoreApplication, QPalette, QColor):
    """Apply application level fixes on the QPalette."""
    # See issue #139
    color = DarkPalette.COLOR_SELECTION_LIGHT
    qcolor = QColor(color)
    app = QCoreApplication.instance()

    if app:
        palette = app.palette()
        palette.setColor(QPalette.Normal, QPalette.Link, qcolor)
        app.setPalette(palette)


def load_stylesheet_from_environment(is_pyqtgraph=False):
    """
    Load the stylesheet from QT_API (or PYQTGRAPH_QT_LIB) environment variable.

    :param is_pyqtgraph: True if it is to be set using PYQTGRAPH_QT_LIB

    :raise KeyError: if QT_API/PYQTGRAPH_QT_LIB does not exist

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_from_environment() will be deprecated in version 3,"
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    qt_api = ''
    pyqtgraph_qt_lib = ''

    loader = ""

    # Get values from QT_API
    try:
        qt_api = os.environ['QT_API']
    except KeyError as err:
        # Log this error just if using QT_API
        if not is_pyqtgraph:
            _logger().error("QT_API does not exist, do os.environ['QT_API']= "
                            "and choose one option from %s", QT_API_VALUES)
    else:
        if not is_pyqtgraph:
            if qt_api in QT_API_VALUES:
                QT_ABSTRACTION = "qtpy"
                _logger().info("Found QT_API='%s'", qt_api)
                loader = _qt_wrapper_import(qt_api)
            else:
                # Raise this error because the function need this key/value
                raise KeyError("QT_API=%s is unknown, please use a value "
                               "from %s",
                               (qt_api, QT_API_VALUES))

    # Get values from PYQTGRAPH_QT_LIB
    try:
        pyqtgraph_qt_lib = os.environ['PYQTGRAPH_QT_LIB']
    except KeyError as err:
        # Log this error just if using PYQTGRAPH_QT_LIB
        if is_pyqtgraph:
            _logger().error("PYQTGRAP_QT_API does not exist, do "
                            "os.environ['PYQTGRAPH_QT_LIB']= "
                            "and choose one option from %s",
                            QT_LIB_VALUES)
    else:

        if is_pyqtgraph:
            if pyqtgraph_qt_lib in QT_LIB_VALUES:
                QT_ABSTRACTION = "pyqtgraph"
                _logger().info("Found PYQTGRAPH_QT_LIB='%s'", pyqtgraph_qt_lib)
                loader = _qt_wrapper_import(pyqtgraph_qt_lib)
            else:
                # Raise this error because the function need this key/value
                raise KeyError("PYQTGRAPH_QT_LIB=%s is unknown, please use a "
                               "value from %s", (
                                   pyqtgraph_qt_lib,
                                   QT_LIB_VALUES))

    # Just a warning if both are set but differs each other
    if qt_api and pyqtgraph_qt_lib:
        if qt_api != pyqtgraph_qt_lib.lower():
            _logger().warning("Both QT_API=%s and PYQTGRAPH_QT_LIB=%s are set, "
                              "but with different values, this could cause "
                              "some issues if using them in the same project!",
                              qt_api, pyqtgraph_qt_lib)

    return loader


def load_stylesheet(pyside=True):
    """
    Load the stylesheet. Takes care of importing the rc module.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet() will not receive pyside parameter in version 3. "
        "Set QtPy environment variable to specify the Qt binding insteady.",
        PendingDeprecationWarning
    )

    # Compiles SCSS/SASS files to QSS
    from qdarkstyle.utils.scss import create_qss
    create_qss()

    # Smart import of the rc file

    pyside_ver = None

    if pyside:

        # Detect the PySide version available
        try:
            import PySide
        except ImportError:  # Compatible with py27
            import PySide2
            pyside_ver = 2
        else:
            pyside_ver = 1

        if pyside_ver == 1:
            import qdarkstyle.pyside_style_rc
        else:
            import qdarkstyle.pyside2_style_rc
    else:
        import qdarkstyle.pyqt_style_rc

    # Load the stylesheet content from resources
    if not pyside:
        from PyQt4.QtCore import QCoreApplication, QFile, QTextStream
        from PyQt4.QtGui import QColor, QPalette
    else:
        if pyside_ver == 1:
            from PySide.QtCore import QCoreApplication, QFile, QTextStream
            from PySide.QtGui import QColor, QPalette
        else:
            from PySide2.QtCore import QCoreApplication, QFile, QTextStream
            from PySide2.QtGui import QColor, QPalette

    # Apply palette fix. See issue #139
    _apply_palette_fix(QCoreApplication, QPalette, QColor)

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()

        # Apply OS specific patches
        stylesheet = _apply_stylesheet_patches(stylesheet)

        return stylesheet


def load_stylesheet_pyside():
    """
    Load the stylesheet for use in a pyside application.

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyside() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    return load_stylesheet(pyside=True)


def load_stylesheet_pyside2():
    """
    Load the stylesheet for use in a pyside2 application.

    :raise NotImplementedError: Because it is not supported yet
    """
    warnings.warn(
        "load_stylesheet_pyside2() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    return load_stylesheet(pyside=True)


def load_stylesheet_pyqt():
    """
    Load the stylesheet for use in a pyqt4 application.

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    return load_stylesheet(pyside=False)


def load_stylesheet_pyqt5():
    """
    Load the stylesheet for use in a pyqt5 application.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt5() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    # Compiles SCSS/SASS files to QSS
    from qdarkstyle.utils.scss import create_qss
    create_qss()

    # Smart import of the rc file
    import qdarkstyle.pyqt5_style_rc

    # Load the stylesheet content from resources
    from PyQt5.QtCore import QCoreApplication, QFile, QTextStream
    from PyQt5.QtGui import QColor, QPalette

    # Apply palette fix. See issue #139
    _apply_palette_fix(QCoreApplication, QPalette, QColor)

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()

        # Apply OS specific patches
        # stylesheet = _apply_stylesheet_patches(stylesheet)
        return stylesheet


def _import_qt_modules_from(use_binding='pyqt5', use_abstraction='qtpy'):
    """New approach to import modules using importlib."""

    if not sys.version_info >= (3, 4):
        print('Function not available for Python < 3.4')

    spec_binding = importlib.util.find_spec(use_binding)
    spec_abstraction = importlib.util.find_spec(use_abstraction)

    if spec_binding is None:
        print("Cannot find Qt binding: ", use_binding)
    else:
        module = importlib.util.module_from_spec(spec_binding)
        spec.loader.exec_module(module)
        # Adding the module to sys.modules is optional.
        sys.modules[name] = module

    if spec_abstraction is None:
        print("Cannot find Qt abstraction layer: ", use_abstraction)
    else:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Adding the module to sys.modules is optional.
        sys.modules[name] = module
