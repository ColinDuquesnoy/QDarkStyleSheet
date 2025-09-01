QDarkStyleSheet
===============

|Build Status| |Docs Status| |Latest PyPI version| |License: MIT|
|License: CC BY 4.0| |Conduct|

The most complete dark/light style sheet for Qt applications supporting Python and C++.

QDarkStyleSheet now works as a complete theme framework supporting:
- Built-in dark and light themes
- Custom palette creation with full color control
- Asset generation for custom themes
- Cross-platform Qt binding compatibility

`Check out the complete documentation. <https://qdarkstylesheet.readthedocs.io/en/latest/screenshots.html>`__


Requirements
------------

**Python Requirements:**
- Python 3.6 or higher

**Qt Requirements:**
- Qt5 or Qt6

**Supported Python Qt Bindings:**
- PyQt5, PyQt6 (recommended)
- PySide2, PySide6 (recommended)
- QtPy (abstraction layer)
- PyQtGraph, Qt.Py (abstraction layers)

**C++ Usage:** Use the generated .qss files directly in your Qt C++ applications.

**Note:** Python 2 and Qt4 (PyQt4, PySide) are no longer supported.
For legacy support, use QDarkStyle version 3.1 or earlier.


What is new?
------------


Version 3
~~~~~~~~~

In the current version 3, `qdarkstyle` is now working as a theme framework,
currently for dark/light themes, keeping styled widgets identical throughout
theme colors.

The palette has been redefined and improved (UI/UX) to accept more colors
and to be able to implement new themes thanks to the
`Spyder team <https://github.com/spyder-ide/spyder>`__ collaboration.

**New in Version 3:**
- Complete custom palette system with asset generation
- Support for custom color schemes and themes
- Enhanced palette framework with built-in color systems
- Improved Qt6 support (PyQt6, PySide6)

The current stable version is using Python 3.6+ and Qt5
(PyQt5 and PySide 2). Also in this version, an option for Qt6 (PyQt6, PySide6)
was added.

The current version for use with Qt6 may still present instabilities.

**Note:** Python 2 and Qt4 (PyQt4 and PySide) are no longer supported.
For legacy support, use QDarkStyle version 3.1 or earlier.

Version 2
~~~~~~~~~

We moved to QtPy to simplify your code in v2.8, thus this is a required
dependency now. We included special patches in three main categories:
operating system, Qt/binding version, application.

Included in that, lots of widgets' styles were included/fixed. A Qt
application example (Python only) with almost all types of widgets and
combinations were included to serve as a portfolio and a checklist for
new styles.

We have added SCSS in v2.7, so the palette can be accessed programmatically.
Also, many scripts were added to give freedom to developers who want to
change the colors of our palette. All images and icons were revised, also
creating SVG files for all of them.

In version 2.6 and later, a restructure stylesheet is provided. The
palette has only 9 colors. Most widgets are revised and their styles
were improved. We also provide a command line (script) to get info that
could be used when opening issues.

**Note:** Version 2 supported Python 2 and Python 3. Python 2 support was removed in Version 3.


Version 1
~~~~~~~~~

First stable release of QDarkStyle.


Installation
------------


Python
~~~~~~

From PyPI: Get the latest stable version of ``qdarkstyle`` package using
*pip* (preferable):

    .. code:: bash

        pip install qdarkstyle


From code: Download/clone the project, go to ``qdarkstyle`` folder then:

-  You can use the *setup* script and pip install.

    .. code:: bash

        pip install .


-  Or, you can use the *setup* script with Python:

    .. code:: bash

        python setup.py install


C++
~~~

- Download/clone the project and copy the following files to your
  application directory (keep the existing directory hierarchy).
  Substitute the all the **THEME** words by the currently available
  (dark/light) the theme you need to use.

    -  **qdarkstyle/THEME/THEMEstyle.qss**
    -  **qdarkstyle/THEME/THEMEstyle.qrc**
    -  **qdarkstyle/THEME/rc/** (the whole directory)


-  Add **qdarkstyle/THEME/THEMEstyle.qrc** to your **.pro file** as follows:

    .. code:: c++

        RESOURCES += qdarkstyle/THEME/THEMEstyle.qrc


-  Load the stylesheet:

    .. code:: c++

        QFile f(":qdarkstyle/THEME/THEMEstyle.qss");

        if (!f.exists())   {
            printf("Unable to set stylesheet, file not found\n");
        }
        else   {
            f.open(QFile::ReadOnly | QFile::Text);
            QTextStream ts(&f);
            qApp->setStyleSheet(ts.readAll());
        }


Note: The ":" in the file name is necessary to define that file as a
resource library. For more information see the discussion
`here <https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/87>`__.


Usage in applications
---------------------


If your project already uses QtPy or you need to set it programmatically,
it is far more simple

.. code:: python

    import sys
    import qdarkstyle
    import os

    # set the environment variable to use a specific wrapper
    # it can be set to pyqt, pyqt5, pyside or pyside2 (not implemented yet)
    # you do not need to use QtPy to set this variable
    os.environ['QT_API'] = 'pyqt5'

    # import from QtPy instead of doing it directly
    # note that QtPy always uses PyQt5 API
    from qtpy import QtWidgets

    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # setup stylesheet
    # the default system in qdarkstyle uses qtpy environment variable
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # run
    window.show()
    app.exec_()


If you are using PyQt5 directly, see the complete example

.. code:: python

    import sys
    import qdarkstyle
    from PyQt5 import QtWidgets

    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    # run
    window.show()
    app.exec_()

**Using Different Built-in Palettes:**

.. code:: python

    from qdarkstyle.dark.palette import DarkPalette
    from qdarkstyle.light.palette import LightPalette

    # Load dark theme (default)
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=DarkPalette))
    
    # Load light theme
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette))
    
    # Combine with Qt API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette))


Here is an example using PySide2

.. code:: python

    import sys
    import qdarkstyle
    from PySide2 import QtWidgets

    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

    # run
    window.show()
    app.exec_()


If you use PyQtGraph, then the code is

.. code:: python

    import sys
    import qdarkstyle
    import os

    # set the environment variable to use a specific wrapper
    # it can be set to PyQt, PyQt5, PySide or PySide2 (not implemented yet)
    os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'

    # import from pyqtgraph instead of doing it directly
    # note that PyQtGraph always uses PyQt4 API
    from pyqtgraph.Qt import QtGui

    # create the application and the main window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ['PYQTGRAPH_QT_LIB'])

    # run
    window.show()
    app.exec_()

If you are using Qt.py, which is different from qtpy, you should install
qtpy then set both to the same binding.


Using Custom Palettes
---------------------

QDarkStyleSheet supports creating completely custom color schemes. Custom palettes allow you to define your own color themes with full control over all colors.

**Basic Custom Palette Example:**

.. code:: python

    from qdarkstyle.palette import Palette

    class DarkNeonPalette(Palette):
        """Cyberpunk neon dark theme."""
        
        ID = 'dark'  # Must use 'dark' for dark themes
        
        # Define your custom colors
        COLOR_BACKGROUND_1 = '#0d0d0d'  # Almost black
        COLOR_BACKGROUND_2 = '#1a1a1a'  # Very dark gray
        COLOR_BACKGROUND_3 = '#262626'  # Dark gray
        COLOR_BACKGROUND_4 = '#333333'  # Medium gray
        COLOR_BACKGROUND_5 = '#404040'  # Light gray
        COLOR_BACKGROUND_6 = '#4d4d4d'  # Lighter gray
        
        COLOR_TEXT_1 = '#ffffff'        # Pure white
        COLOR_TEXT_2 = '#e6e6e6'        # Light gray
        COLOR_TEXT_3 = '#cccccc'        # Medium gray
        COLOR_TEXT_4 = '#b3b3b3'        # Darker gray
        
        COLOR_ACCENT_1 = '#ff0080'      # Hot pink
        COLOR_ACCENT_2 = '#e6006b'      # Dark pink
        COLOR_ACCENT_3 = '#cc0066'      # Darker pink
        COLOR_ACCENT_4 = '#b30055'      # Very dark pink
        COLOR_ACCENT_5 = '#990044'      # Almost black pink
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 230

    class LightNeonPalette(Palette):
        """Cyberpunk neon light theme."""
        
        ID = 'light'  # Must use 'light' for light themes
        
        # Light backgrounds with neon accents
        COLOR_BACKGROUND_1 = '#ffffff'  # Pure white
        COLOR_BACKGROUND_2 = '#f8f8f8'  # Very light gray
        COLOR_BACKGROUND_3 = '#f0f0f0'  # Light gray
        COLOR_BACKGROUND_4 = '#e8e8e8'  # Medium light gray
        COLOR_BACKGROUND_5 = '#e0e0e0'  # Medium gray
        COLOR_BACKGROUND_6 = '#d8d8d8'  # Darker gray
        
        # Dark text colors for light background
        COLOR_TEXT_1 = '#0d0d0d'        # Almost black
        COLOR_TEXT_2 = '#1a1a1a'        # Very dark gray
        COLOR_TEXT_3 = '#262626'        # Dark gray
        COLOR_TEXT_4 = '#333333'        # Medium gray
        
        # Same neon accent colors for consistency
        COLOR_ACCENT_1 = '#ff0080'      # Hot pink
        COLOR_ACCENT_2 = '#e6006b'      # Dark pink
        COLOR_ACCENT_3 = '#cc0066'      # Darker pink
        COLOR_ACCENT_4 = '#b30055'      # Very dark pink
        COLOR_ACCENT_5 = '#990044'      # Almost black pink
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 230

**Generate and Use Custom Themes:**

.. code:: bash

    # Generate dark theme assets
    python -m qdarkstyle.utils \
        --custom-palette-file my_theme.py \
        --custom-palette-class-name DarkNeonPalette \
        --base-path ./my_neon_theme

    # Generate light theme assets
    python -m qdarkstyle.utils \
        --custom-palette-file my_theme.py \
        --custom-palette-class-name LightNeonPalette \
        --base-path ./my_neon_theme

**Use with load_stylesheet() (Recommended):**

.. code:: python

    # Import your custom palettes
    from my_theme import DarkNeonPalette, LightNeonPalette
    
    # Use with load_stylesheet() - works because IDs are 'dark'/'light'
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=DarkNeonPalette))
    # or
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightNeonPalette))

**Or load QSS files directly:**

.. code:: python

    # Load dark theme
    with open('./my_neon_theme/dark/darkstyle.qss', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    
    # Load light theme
    with open('./my_neon_theme/light/lightstyle.qss', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

.. note::
   Custom palettes with 'dark'/'light' IDs work with ``qdarkstyle.load_stylesheet()``, others require direct QSS loading.

For complete custom palette documentation, see the `Custom Palettes Guide <https://qdarkstylesheet.readthedocs.io/en/latest/custom_palettes.html>`__.


Usage of example/portfolio
--------------------------


There is an example included in the package. You only need to have PySide2 or
PyQt5 is installed on your system.

.. code:: bash

    # dark theme example
    $ qdarkstyle.example --palette=dark

    # light theme example
    $ qdarkstyle.example --palette=light

    # no theme/style sheet applied
    $ qdarkstyle.example --palette=none

    # check all options included
    $ qdarkstyle.example --help

Custom Themes Demo
------------------

For a comprehensive demonstration of custom theme creation, run the custom themes demo:

.. code:: bash

    python scripts/custom_themes_demo.py

This demo showcases:
- Three complete theme examples (Ocean, Forest, Sunset)
- Real-time theme switching
- Complete workflow from palette definition to application
- Comprehensive UI widget testing

For more information, see the :doc:`Custom Themes Demo documentation <scripts/custom_themes_demo>`.


Changelog
---------

Please, see `CHANGES <CHANGES.rst>`__ file.


License
-------

This project is licensed under the MIT license. Images contained in this
project is licensed under CC-BY license.

For more information see `LICENSE <LICENSE.rst>`__ file.


Authors
-------

For more information see `AUTHORS <AUTHORS.rst>`__ file.


Contributing
------------

Most widgets have been styled. If you find a widget that has not been
style, just open an issue on the issue tracker or, better, submit a pull
request.

If you want to contribute, see `CONTRIBUTING <CONTRIBUTING.rst>`__ file.

.. |Build Status| image:: https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet.png?branch=master
   :target: https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet
.. |Docs Status| image:: https://readthedocs.org/projects/qdarkstylesheet/badge/?version=latest&style=flat
   :target: https://qdarkstylesheet.readthedocs.io
.. |Latest PyPI version| image:: https://img.shields.io/pypi/v/QDarkStyle.svg
   :target: https://pypi.python.org/pypi/QDarkStyle
.. |License: MIT| image:: https://img.shields.io/dub/l/vibe-d.svg?color=lightgrey
   :target: https://opensource.org/licenses/MIT
.. |License: CC BY 4.0| image:: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
   :target: https://creativecommons.org/licenses/by/4.0/
.. |Conduct| image:: https://img.shields.io/badge/code%20of%20conduct-contributor%20covenant-green.svg?style=flat&color=lightgrey
   :target: http://contributor-covenant.org/version/1/4/
