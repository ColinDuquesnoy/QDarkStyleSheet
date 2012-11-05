A dark stylesheet for Qt applications. 

Screenshots
===================

**TODO: Add screenshots**

Usage
============

- Download/clone the project next to your main executable (or wherever you find it fits well)
- Load QDarkStyleSheets/style.qss and apply it on your QApplication instance

Here is a quick snippet in python (PySide/PyQt) that shows how to use the stylesheet:

```Python
def main():
    # create the qt application
    app = QApplication()
    # Load the stylesheet
    f = open("QDarkStyleSheet/style.qss","r")
    style_sheet = f.read()
    f.close()
    # apply it
    app.setStyleSheet(style_sheet)
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
 - QTableView
 - QToolBox 

Contact information:
===========================

  - Maintainer: colin.duquesnoy@gmail.com
  - Homepage: https://github.com/ColinDuquesnoy/QDarkStyleSheet