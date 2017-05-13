QDarkStylesheet
===============

[![Build Status](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet.png?branch=master)](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)
[![Latest PyPI version](https://img.shields.io/pypi/v/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)

A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PyQt4 and PyQt5).


License
=======

This project is licensed under the MIT license.


Installation
============

Python
------

Install ``qdarkstyle`` package using the *setup* script or using *pip*:

```bash
python setup.py install
```

or

```bash
pip install qdarkstyle
```

C++
---

1) Download/clone the project and copy the following files to your application directory (keep the existing directory hierarchy):

 - **qdarkstyle/style.qss**
 - **qdarkstyle/style.qrc**
 - **qdarkstyle/rc/** (the whole directory)

2) Add **qdarkstyle/style.qrc** to your **.pro file**

3) Load the stylesheet:

```cpp
QFile f(":qdarkstyle/style.qss");
if (!f.exists())
{
    printf("Unable to set stylesheet, file not found\n");
}
else
{
    f.open(QFile::ReadOnly | QFile::Text);
    QTextStream ts(&f);
    qApp->setStyleSheet(ts.readAll());
}

```



Usage
=====

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

and
```Python
from PySide import QtGui
```

by

```Python
from PyQt4 import QtGui
```

To use PyQt5, you need to use ``load_stylesheet_pyqt5`` instead of
``load_stylesheet``.

```Python
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
```

_There is an example included in the *example* folder.
You can run the script without installing qdarkstyle. You only need to have
PySide (or PyQt4 or PyQt5) installed on your system._

Status:
=======

Most widgets have been styled. If you find a widget that has not been
style, just open an issue on the issue tracker or, better, submit a pull
request.

Changelog
=========

* 2.3.1:
    - Improve checkbox color (use accent color used in other widgets) and darken view hover/selected colors to play nicer with other widget colors
    - Shift to the right the first tab
    - Update license year
    - Update README.md (fix snapshots links and formatting)
    - Removed QLineEdit top/bottom padding which cut off text while editing QListView items

* 2.3.0:
    - Add support for QDateEdit

* 2.2.2:
    - Add hover to unselected item in QListView/QTreeView
    - Fixes for vertical QToolBar, QToolBar Extend Button & QTabWidget's Pane Misalignment
    - Fixed consistency of QTabBar depending on position

* 2.2.1:
    - remove border of status bar widgets

* 2.2:
    - Major update of the color scheme based on the Breeze Dark theme of KDE 5
    - fix issues #29, #30, #31, #32 and #35
* 2.1:
    - Add style for QPushButton:checked
    - Improve QCheckBox and QRadioButton style
    - Add style for QMenu::right-arrow
* 2.0: Improve stylesheet to make it look a bit more modern (see pull request #25)
* 1.16: fix QGroupBox title padding (see issue #20)
* 1.15: improve tristate checkbox graphics: undetermined state is now represented by a dash
* 1.14: add support for tristate check boxes and for vertical and horizontal lines
* 1.13: fix issue with horizontal scrollbar arrows, left and right were inversed.
* 1.12: fix minimum size of input widgets (see issue #14)
* 1.11:
    - Fix QDockWidget title position on Mac.
    - Add QStatusBar support
    - Improve QToolButton especially the MenuButtonPopup and InstantPopup modes
* 1.10:
    - Add PyQt5 support
    - Fix bug #12 (dock widget title not dark on OSX. Note that this reopens
      issue #8 for MAC users)
* 1.9:
    - Improve QTabBar consistency and make selected tabs more distinctive
* 1.8:
    - Add support for QToolBox
    - Fix issue with grid line in QTableView if there is only ONE row/column
* 1.7:
    - Fix appearance of bottom tab bars (invert gradient)
    - Improve QTableView: add grid line and fix section borders
    - Fix bug #7: bug when resizing QTableView
    - Fix bug #8: text elidation no working on QDockWidget
* 1.6:
    - Improve QToolButton style
    - Add support for InstantPopup and MenuButtonPopup
    - Improve QMenu style (better spacing with icons)
    - Add __version__ to python package.
* 1.5:
    - improve QTabBar style: now works with all tab bar positions (North, South, West and East)
    - fix bug #6: hide QTabBar base to avoid stange lines at the base of the tab bar.
* 1.4: Add style.qss to qrc file, this fix issues with cx_freeze
* 1.3:
    - remove outline on button, checkbox and radio button
    - add support for closable tabs
    - better disabled buttons
    - fix QTextEdit background color to match the color of QPlainTextEdit and QLineEdit
    - better hover/selected states for QTreeView and QListView
    - add QHeaderView support
* 1.2:
   - Improve QTableView support
* 1.1:
   - Switch to MIT license
   - Add python 3 support
* 1.0:
  - First public release (LGPL v2)




Contact information:
====================

  - Maintainer: colin.duquesnoy@gmail.com
  - Homepage: https://github.com/ColinDuquesnoy/QDarkStyleSheet


Snapshots
=========

Here are a few snapshots:

![alt text](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/screenshots/QDarkStyle%20example%201.png "QDarkStyle example 1")
![alt text](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/screenshots/QDarkStyle%20example%202.png "QDarkStyle example 2")
