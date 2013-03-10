"""
Initialise the QDarkStyleSheet module when used with python.

This modules provides a function to transparently load the stylesheets
with the correct rc file.
"""
import os


def load_stylesheet(pyside=True):
    """
    Loads the stylesheet. Takes care of importing the rc module.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    # Smart import of the rc file
    if pyside:
        try:
            import style_pyside_rc
        except ImportError:
            style_pyside_rc = None
            print "Failed to load PySide rc file, stylesheets won't use any icons"
    else:
        try:
            import style_pyqt_rc
        except ImportError:
            style_pyqt_rc = None
            print "Failed to load PyQt4 rc file, stylesheets won't use any icons"

    # Load the stylesheet content
    ret_val = ""
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "style.qss")
    with open(os.path.join(__file__, filename)) as stylesheet:
        ret_val = stylesheet.read()
    return ret_val
