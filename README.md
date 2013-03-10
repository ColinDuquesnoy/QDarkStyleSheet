A dark stylesheet for Qt applications. 

Usage
============

- Download/clone the project next to your main executable (or wherever you find it fits well)
- Compile the qrc file for your system and add it to your application. (simply run compile_qrc.py script, it will compile the qrc file for use with Qt (c++), PyQt4 and Pyside).
- Load QDarkStyleSheets/style.qss and apply it on your QApplication instance

Here is a quick example using PySide:


```Python
import sys
from PySide import QtGui
# import the style resources comiled by compile_rc.py
import style_pyside_rc

# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
with open("style.qss", 'r') as stylesheet:
    app.setStyleSheet(stylesheet.read())

# run
window.show()
app.exec_()
```

Status:
==============

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
===========================

  - Maintainer: colin.duquesnoy@gmail.com
  - Homepage: https://github.com/ColinDuquesnoy/QDarkStyleSheet

Screenshots
===================

I have used this stylesheet for an internal tool at work. Are are a few screenshots:

![alt text](/screenshots/01.png "Screenshot 01")
