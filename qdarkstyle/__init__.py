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

import logging
import os
import platform
import sys
import warnings
import copy

if sys.version_info >= (3, 4):
    import importlib

__version__ = "2.6.6"


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
        from PyQt4.QtCore import QFile, QTextStream
    else:
        if pyside_ver == 1:
            from PySide.QtCore import QFile, QTextStream
        else:
            from PySide2.QtCore import QFile, QTextStream

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
        if platform.system().lower() == 'darwin':  # see issue #12 on github
            mac_fix = '''
            QDockWidget::title
            {
                background-color: #32414B;
                text-align: center;
                height: 12px;
            }
            '''
            stylesheet += mac_fix
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
    # Smart import of the rc file
    import qdarkstyle.pyqt5_style_rc

    # Load the stylesheet content from resources
    from PyQt5.QtCore import QFile, QTextStream

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
        if platform.system().lower() == 'darwin':  # see issue #12 on github
            mac_fix = '''
            QDockWidget::title
            {
                background-color: #32414B;
                text-align: center;
                height: 12px;
            }
            '''
            stylesheet += mac_fix
        return stylesheet


def information():
    """Get system and runtime information."""
    info = []
    qt_api = ''
    qt_lib = ''
    qt_bin = ''

    try:
        qt_api = os.environ['QT_API']
    except KeyError:
        qt_api = 'Not set or nonexistent'

    try:
        from Qt import __binding__
    except Exception:
        # It should be (KeyError, ModuleNotFoundError, ImportError)
        # but each python version have a different one, and not define others
        qt_lib = 'Not set or nonexistent'
    else:
        qt_lib = __binding__

    try:
        qt_bin = os.environ['PYQTGRAPH_QT_LIB']
    except KeyError:
        qt_bin = 'Not set or nonexistent'

    info.append('QDarkStyle: %s' % __version__)
    info.append('OS: %s %s %s' % (platform.system(), platform.release(), platform.machine()))
    info.append('Platform: %s' % sys.platform)
    info.append('Python: %s' % '.'.join(str(e) for e in sys.version_info[:]))
    info.append('Python API: %s' % sys.api_version)

    info.append('Binding in use:     %s' % QT_BINDING)
    info.append('Abstraction in use: %s' % QT_ABSTRACTION)

    info.append('qtpy (QT_API):                %s' % qt_api)
    info.append('pyqtgraph (PYQTGRAPH_QT_LIB): %s' % qt_lib)
    info.append('Qt.py (__binding__):          %s' % qt_bin)

    return info


def qt_bindings():
    """Return a list of qt bindings available."""
    return _check_imports(import_list=QT_BINDINGS)


def qt_abstractions():
    """Return a list of qt abstraction layers available."""
    return _check_imports(import_list=QT_ABSTRACTIONS)


def _check_imports(import_list):
    """Return a list of imports available."""

    # Disable warnings here
    warnings.filterwarnings("ignore")

    import_list_return = copy.deepcopy(import_list)
    # Using import_list_return var in for, does not work in py2.7
    # when removing the element, it reflects on for list
    # so it skips next element
    for current_import in import_list:

        spec = True
        # Copy the sys path to make sure to not insert anything
        sys_path = sys.path

        # Check import
        if sys.version_info >= (3, 4):
            spec = importlib.util.find_spec(current_import)
        else:
            try:
                __import__(current_import)
            except RuntimeWarning:
                spec = True
            except Exception:
                spec = None
            else:
                spec = True

        if spec is None:
            # Remove if not available
            import_list_return.remove(current_import)

        # Restore sys path
        sys.path = sys_path

    # Restore warnings
    warnings.resetwarnings()

    return import_list_return


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
