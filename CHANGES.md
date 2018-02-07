Changelog
=========

* 2.5.1:
    - Fix travis files, needs more improvement #74
    - Improve modules description
    - Update setup.py, remove license
    - Improve README, CHANGES and AUTHORS
* 2.5:
    - Add new complete example with new files
    - Add new screenshots for new example
    - Update travis files
    - Add support to example of QtPy and PyQtGraph
    - Move scripts for compiling to scrip folder
    - Update README, CHANGES
* 2.4:
    - Add function to get Qt information from environment variable #69, #70, #73
    - Add CC-BY license for images and transfer COPYING to LICENSE file #68
    - Fix tabs style - selected tab color and shift #59, #72
    - Restructure README creating AUTHORS, CHANGES, and LICENSE #71
* 2.3.1:
    - Improve checkbox color (use accent color used in other widgets) and darken view hover/selected colors to play nicer with other widget colors
    - Shift to the right the first tab
    - Update license year
    - Update README (fix snapshots links and formatting)
    - Removed QLineEdit top/bottom padding which cut off text while editing QListView items
* 2.3.0:
    - Add support for QDateEdit
* 2.2.2:
    - Add hover to unselected item in QListView/QTreeView
    - Fixes for vertical QToolBar, QToolBar Extend Button & QTabWidget's Pane Misalignment
    - Fixed consistency of QTabBar depending on position
* 2.2.1:
    - Remove border of status bar widgets
* 2.2:
    - Major update of the color scheme based on the Breeze Dark theme of KDE 5
    - Fix issues #29, #30, #31, #32 and #35
* 2.1:
    - Add style for QPushButton:checked
    - Improve QCheckBox and QRadioButton style
    - Add style for QMenu::right-arrow
* 2.0:
    - Improve stylesheet to make it look a bit more modern (see pull request #25)
* 1.16:
    - Fix QGroupBox title padding (see issue #20)
* 1.15:
    - Improve tristate checkbox graphics: undetermined state is now represented by a dash
* 1.14:
    - Add support for tristate check boxes and for vertical and horizontal lines
* 1.13:
    - Fix issue with horizontal scrollbar arrows, left and right were inversed.
* 1.12:
    - Fix minimum size of input widgets (see issue #14)
* 1.11:
    - Fix QDockWidget title position on Mac.
    - Add QStatusBar support
    - Improve QToolButton especially the MenuButtonPopup and InstantPopup modes
* 1.10:
    - Add PyQt5 support
    - Fix bug #12 (dock widget title not dark on OSX. Note that this reopens issue #8 for MAC users)
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
    - Add \__version__ to python package.
* 1.5:
    - Improve QTabBar style: now works with all tab bar positions (North, South, West and East)
    - Fix bug #6: hide QTabBar base to avoid stange lines at the base of the tab bar.
* 1.4:
    - Add style.qss to qrc file, this fix issues with cx_freeze
* 1.3:
    - Remove outline on button, checkbox and radio button
    - Add support for closable tabs
    - Better disabled buttons
    - Fix QTextEdit background color to match the color of QPlainTextEdit and QLineEdit
    - Better hover/selected states for QTreeView and QListView
    - Add QHeaderView support
* 1.2:
    - Improve QTableView support
* 1.1:
    - Switch to MIT license
    - Add python 3 support
* 1.0:
    - First public release (LGPL v2)
