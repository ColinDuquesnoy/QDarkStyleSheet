# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
Initialise the QDarkStyleSheet module when used with python.

This modules provides a function to transparently load the stylesheets
with the correct rc file.
"""
import logging
import platform
import os


__version__ = "2.4"

PYQTGRAPH_QT_LIB_VALUES = ['PyQt', 'PyQt5', 'PySide', 'PySide2']
QT_API_VALUES = ['pyqt', 'pyqt5', 'pyside', 'pyside2']


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
        _logger().error("Impossible import Qt wrapper. " + str(err))
    else:
        _logger().info("Using Qt wrapper = %s " % qt_wrapper)
    finally:
        return loader


def load_stylesheet_from_environment(is_pyqtgraph=False):
    """
    Load the stylesheet from QT_API (or PYQTGRAPH_QT_LIB) environment variable.

    :param is_pyqtgraph: True if it is to be set using PYQTGRAPH_QT_LIB

    :raise KeyError: if QT_API/PYQTGRAPH_QT_LIB does not exist

    :return the stylesheet string
    """
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
                            "and choose one option from %s" % QT_API_VALUES)
    else:
        if not is_pyqtgraph:
            if qt_api in QT_API_VALUES:
                _logger().info("Found QT_API='%s'" % qt_api)
                loader = _qt_wrapper_import(qt_api)
            else:
                # Raise this error because the function need this key/value
                raise KeyError("QT_API=%s is unknown, please use a value "
                               "from %s" % (qt_api, QT_API_VALUES))

    # Get values from PYQTGRAPH_QT_LIB
    try:
        pyqtgraph_qt_lib = os.environ['PYQTGRAPH_QT_LIB']
    except KeyError as err:
        # Log this error just if using PYQTGRAPH_QT_LIB
        if is_pyqtgraph:
            _logger().error("PYQTGRAP_QT_API does not exist, do "
                            "os.environ['PYQTGRAPH_QT_LIB']= "
                            "and choose one option from %s" %
                            PYQTGRAPH_QT_LIB_VALUES)
    else:
        if is_pyqtgraph:
            if pyqtgraph_qt_lib in PYQTGRAPH_QT_LIB_VALUES:
                _logger().info("Found PYQTGRAPH_QT_LIB='%s'" % pyqtgraph_qt_lib)
                loader = _qt_wrapper_import(pyqtgraph_qt_lib)
            else:
                # Raise this error because the function need this key/value
                raise KeyError("PYQTGRAPH_QT_LIB=%s is unknown, please use a "
                               "value from %s" % (pyqtgraph_qt_lib,
                                                  PYQTGRAPH_QT_LIB_VALUES))

    # Just a warning if both are set but differs each other
    if qt_api and pyqtgraph_qt_lib:
        if qt_api != pyqtgraph_qt_lib.lower():
            _logger().warning("Both QT_API=%s and PYQTGRAPH_QT_LIB=%s are set, "
                              "but with different values, this could cause "
                              "some issues if using them in the same project!"
                              % (qt_api, pyqtgraph_qt_lib))

    return loader


def load_stylesheet(pyside=True):
    """
    Load the stylesheet. Takes care of importing the rc module.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    # Smart import of the rc file
    if pyside:
        import qdarkstyle.pyside_style_rc
    else:
        import qdarkstyle.pyqt_style_rc

    # Load the stylesheet content from resources
    if not pyside:
        from PyQt4.QtCore import QFile, QTextStream
    else:
        from PySide.QtCore import QFile, QTextStream

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
                background-color: #31363b;
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
    return load_stylesheet(pyside=True)


def load_stylesheet_pyside2():
    """
    Load the stylesheet for use in a pyside2 application.

    :raise NotImplementedError: Because it is not supported yet
    """
    raise NotImplementedError("PySide 2 is not supported yet.")


def load_stylesheet_pyqt():
    """
    Load the stylesheet for use in a pyqt4 application.

    :return the stylesheet string
    """
    return load_stylesheet(pyside=False)


def load_stylesheet_pyqt5():
    """
    Load the stylesheet for use in a pyqt5 application.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
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
                background-color: #31363b;
                text-align: center;
                height: 12px;
            }
            '''
            stylesheet += mac_fix
        return stylesheet
