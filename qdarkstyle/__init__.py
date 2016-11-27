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


__version__ = "2.3.0"


def _logger():
    return logging.getLogger('qdarkstyle')


def load_stylesheet(pyside=True):
    """
    Loads the stylesheet. Takes care of importing the rc module.

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


def load_stylesheet_pyqt5():
    """
    Loads the stylesheet for use in a pyqt5 application.

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
