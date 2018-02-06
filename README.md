QDarkStylesheet
===============

[![Build Status](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet.png?branch=master)](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)
[![Latest PyPI version](https://img.shields.io/pypi/v/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)

A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PyQt4, PyQt5, QtPy,
PyQtGraph).


Installation
============


Python
------

From PyPI: Get the lastest stable version of ``qdarkstyle`` package using *pip* (preferable):

```bash
pip install qdarkstyle
```


From code: Download/clone the project, go to ``qdarkstyle`` folder then:

- You can use the *setup* script and pip install.
    ```bash
    pip install .
    ```

- Or, you can use the *setup* script with Python:
    ```bash
    python setup.py install
    ```


C++
---

1) Download/clone the project and copy the following files to your application
directory (keep the existing directory hierarchy):

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
app.setStyleSheet(qdarkstyle.load_stylesheet_pyside())

# run
window.show()
app.exec_()
```

To use another wrapper for Qt, you just need to replace some lines.
See examples bellow.

To use PyQt4, change two lines:

```Python
from PySide import QtGui
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
```

If PyQt5, more lines need to be changed because of its API,
see the complete example

```Python
import sys
import qdarkstyle
from PyQt5 import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

# run
window.show()
app.exec_()
```

If your project uses QtPy or you need to set it programmatically,
it is far more simple:

```Python

import sys
import qdarkstyle
import os

# set the environment variable to use a specific wrapper
# it can be set to pyqt, pyqt5, pyside or pyside2 (not implemented yet)
# you do not need to use QtPy to set this variable
os.environ['QT_API'] = 'pyqt'

# import from QtPy instead of doing it directly
# note that QtPy always uses PyQt5 API
from qtpy import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())

# run
window.show()
app.exec_()
```

It is also simple if you use PyQtGraph:

```Python
import sys
import qdarkstyle
import os

# set the environment variable to use a specific wrapper
# it can be set to PyQt, PyQt5, PySide or PySide2 (not implemented yet)
os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt' 

# import from pyqtgraph instead of doing it directly
# note that PyQtGraph always uses PyQt4 API
from pyqtgraph.Qt import QtGui

# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True))

# run
window.show()
app.exec_()
```

_There is an example included in the *example* folder.
You can run the script without installing qdarkstyle. You only need to have
PySide (or PyQt4 or PyQt5) installed on your system._


Snapshots
=========

Here are a few snapshots:

![alt text](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/screenshots/QDarkStyle%20example%201.png "QDarkStyle example 1")
![alt text](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/screenshots/QDarkStyle%20example%202.png "QDarkStyle example 2")


Changelog
=========

Please, see [CHANGES](CHANGES.md) file.


License
=======

This project is licensed under the MIT license.
Imagens contained in this project are licensed under CC-BY license.

For more information see [LICENSE](LICENSE.md) file.


Authors
=======

For more information see [AUTHORS](AUTHORS.md) file.


Contribute
==========

Most widgets have been styled. If you find a widget that has not been
style, just open an issue on the issue tracker or, better, submit a pull
request.
