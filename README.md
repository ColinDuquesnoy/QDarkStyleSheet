A dark stylesheet for Qt applications. 

Screenshots
===================

**TODO: Add screenshots**

Usage
============

- Download/clone the project next to your main executable (or wherever you find it fits well)
- Load QDarkStyleSheets/style.qss and
- Format the stylesheet string to give it the correct location (otherwise 
  resources won't show). 
  People that don't want to format may replace all "%(location)s/" occurrences in the style.qss file by their own resource 
  location.
- apply it on your QApplication instance

Here is a quick snippet in python (PySide/PyQt) that shows how to use the 
stylesheet. 


```Python
def main():
    # create the qt application
    app = QApplication()

    # Load the stylesheet
    f = open("QDarkStyleSheet/style.qss","r")
    style_sheet = f.read()
    f.close()

    # format style_sheet to get the correct resource path.
    path = "" # here we use the working directory but it might somewhere else
    style_sheet = style_sheet % {"location":path}
    
    # apply the stylesheet
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
