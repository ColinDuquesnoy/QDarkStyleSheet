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
    cwd = os.path.dirname(os.path.realpath(__file__))
    # Smart import of the rc file
    if pyside:
        import pyside_style_rc
    else:
        import pyqt_style_rc

    # Load the stylesheet content
    ret_val = ""
    filename = os.path.join(cwd, "style.qss")
    with open(os.path.join(__file__, filename)) as stylesheet:
        ret_val = stylesheet.read()
    return ret_val
