QDarkStylesheet
==================

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ColinDuquesnoy/qdarkstylesheet/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
[![Build Status](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet.png?branch=master)](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet)
[![Number of PyPI downloads](https://pypip.in/d/QDarkStyle/badge.png)](https://pypi.python.org/pypi/QDarkStyle)
[![Latest PyPI version](https://pypip.in/v/QDarkStyle/badge.png)](https://pypi.python.org/pypi/QDarkStyle)

A dark stylesheet for Qt applications.


License
===========

This project is licensed under the MIT license.


Installation
==============

Python
-----------

Install the qdarkstyle package using the *setup* script or using *pip*:

```bash
python setup.py install
```

or

```bash
pip install qdarkstyle
```

C++
---------

Download/clone the project and copy the following files to your application directory:

- **qdarkstyle/style.qss**
- **qdarkstyle/style.qrc**
- **qdarkstyle/rc/** (the whole directory)

Usage
============

Here is an example using PySide:


```Python
import sys
import qdarkstyle
from PySide import QtGui


# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet())

# run
window.show()
app.exec_()
```

To use PyQt4 instead of PySide, you just need to replace

```Python
app.setStyleSheet(qdarkstyle.load_stylesheet())
```

by

```Python
app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
```

_There is an example included in the *example* folder. You can run the script without installing qdarkstyle. You
only need to have PySide or PyQt4 installed on your system._

Status:
===========

The following widgets are styled: 

 - QMainWindow
 - QWidget
 - QMenu, QMenuBar
 - QToolTip
 - QAbstractItemView
 - QLineEdit
 - QGroupBox
 - QTextEdit, QPlainTextEdit
 - QTreeView,
 - QScrollBar
 - QRadioButton
 - QCheckBox
 - QComboBox
 - QPushButton
 - QToolButton
 - QToolBar
 - QProgressBar
 - QSpinBox
 - QFrame
 - QTabWidget, QTabBar
 - QDockWidget
 - QSlider (horizontal and vertical)

What still needs to be done:

 - QAbstractScrollArea
 - QSplitter
 - QStatusBar
 - QToolBox 


Contact information:
=========================

  - Maintainer: colin.duquesnoy@gmail.com
  - Homepage: https://github.com/ColinDuquesnoy/QDarkStyleSheet


Snapshots
=================

I have used this stylesheet for an internal tool at work. Are are a few screenshots:

![alt text](/screenshots/01.png "Screenshot 01")




