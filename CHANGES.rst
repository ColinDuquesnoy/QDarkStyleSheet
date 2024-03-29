Changelog
=========
- 3.2.2:
    - Remove explicit PyQt5 import #341
    - Fix setuptools deprecation warning #340
- 3.2.2:
    - Rebuild assets under Qt5 due QtPy limitation #339
- 3.2.1:
    - Add COLOR_DISABLED to vars #337
    - Enhance contributing guide
- 3.2:
    - Improve C++ usage description #329
    - Add Qt6 support, fixes entries and docs
    - Fix warnings calls #325
    - Fix hidden background Qtoolbox MR #324
    - Enhance contrast ligh theme MR #335
    - Drop Python 2 support #327
    - Add constant to disable color of widgets
    - Fixes small typos and shebang cleanup
- 3.1:
    - Fixes generating resources
    - Correct spelling mistakes
    - Refactoring functions from qdarkstyle.utils
    - Include prefix of palette.ID for qrc, qss, _rc files, keep working on C++ #273
    - Fix global variables issue #298
    - Include data files when installing package #299
- 3.0.3:
    - Temporary fix for expanded combo box in Qt 5.15, fixes #282, #285, MR #288
    - Fix generating assets in Posix
    - Fix tristate value for checkbox #275
    - Minor fixes and improvements
- 3.0.2:
    - Enable the use of setTabColor and add example, fixes #212
    - Update description to inform about Python 2 and Qt4 unsupported versions
    - Add missing examples #251
- 3.0.1:
    - Enhancement of state of active/non-active items in views #209
    - Update manifest to include UI files
- **3.0.0**:
    - New structure to create different palettes #268, #164
    - New light palette #240, #268
    - Improved dark palette #252, #266, #264, #265, #248
    - Improved tool buttons #260
    - Improved tabs #270, #271, #267
    - Improved combo boxes #263
    - Improved close/float sizes os-dependent #267
    - Fix checkbox problems #200, #259, #239
    - Fix indicators' colors in menus and tables #242
    - Fix dock widget tab hover #243
    - Workaround for menus with indicators and icons #214
    - Update to be compatible with Qt 5.[12,13,14,15]
- 2.8.1:
    - Fix rst file formats and links #229
    - Add .gitattributes for generated and documentation files
    - Add more complete tox and Travis envs with many checks
    - Fix removing message format argument
    - Fix QGroupBox small indicator size #218
    - Fix QGroupBox incorrect indicator icon when unfocused #219
    - Fix QDateTimeEdit incorrect drop-down arrow icon #220
    - Fix documentation
- 2.8:
    - Fix tooltip giant rectangle #174
    - Fix QTextEdit without borders inside frame #188
    - Fix PyQt5 issues on dropdown #191
    - Fix combo box with icons #169
    - Fix QToolbBar vertical handle #210
    - Fix pane tab label cropped on activation #199
    - Enhance vertical/horizontal lines #184
    - Enhance tool button size and spacing #181, #183, #202
    - Enhance buttons and inputs with focus, blue border #194, #211
    - Enhance QSplitter #207
    - Removed QStatusBar vertical lines #205
- 2.7:
    - Remove utils from import in qdarkstyle, #170
    - Fix border colors in tool button #176
    - Fix scroll area and stacked with 2px padding, #159
    - Fix background submenu color, #179
    - Fix extra border aside header's arrow indicator, #180
    - Fix menu right arrow indicator
    - Fix slide bars colors, #150
    - Fix QLabels problems, #163, #139
    - Fix problems with example settings using PySide2 and --no\_dark #167
    - Provide SVG files for all images, standard names, and sizes, fix images, #149
    - Improve images and add high-resolution images, #140
    - Improve docs
    - Add check to scripts for generating images, #137
    - Fix tox and Travis scripts #76
    - Provide docs in RTD, part of #160
    - Add helpdev dependency for reports and checks, #147
    - Update authors and maintainers
- 2.6.8:
    - Fix double border in QtabWidget for pyqt5
    - Fix widgets border in QTabWidget as QLabel #141, #123, #126
    - Fix QTab scroller buttons background #136
    - Update color from images, fix #127
    - Add retina resolution @2x, fix #140
    - Intermediate version before merge PR #142 adding scripts
- 2.6.7:
    - Fix combobox indicator and padding #132
    - Fix PyQtGraph plot axes covered by padding #134
    - Update authors
- 2.6.6:
    - Fix tabbed borderless frames and add more examples, #123, #126
    - Add feedback to pressed buttons, #133
    - Change future warning to pending deprecation for developers, #125 in v2.x
    - Fix hover in qtabwidget, #128
- 2.6.5:
    - Fix borderless widgets inside QTabWidget, #123
    - Fix palette table inside CSS file, header using the last column
    - Tested on Python 27, 34, 36, 37
- 2.6.4:
    - Python 2.7 compatibility, #121
    - Fix MANIFEST
- 2.6.3:
    - Palette color enhances, better contrast, contribute to #118
    - Fixes Qslider background
    - Better colors and format for tab and toolbox, contribute to #118
- 2.6.2:
    - Enhance command link button
    - Enhance tab colors and spacing, closes #118
    - Start using tox, helping partially #77
    - Fix example and other scripts issues
- 2.6.1:
    - Fix and improve QSplitter and separators from toolbar and windows #115
    - Fix README version screenshots and update them
    - Add reset function into an example to reset GUI settings, after you mess up with
- 2.6:
    - Many other enhancements and fix #103, #111, #106
    - Fix tab disabled, background and color
    - Enhance tab selection
    - Enhance spacing (padding and margin)
    - Enhance table, list, tree and combo box selection
    - Fix slider disabled and enhance size
    - Fix the wrong upload of style.qss - sorry
    - Fix almost all widgets backgrounds and other not previously covered widgets with new style
    - New palette color, almost whole new qss file, simplifies configuration, partially #112, #101, #109,
    - Add changes made by other people in the new style - merge does not work there #93, #92, #102
    - Update README with Qt.py and PySide 2 information #110, #107, #83
    - Update **init** info
    - Improve scripts for processing ui and qrc
    - Add **main** and setup entry, to access the function directly
    - Add function to get information about bindings and abstraction layers for debugging and/or issue tracker
    - PySide 2 support
    - Improve menu indicator position on QPushButton, #102
- 2.5.4
    - Fix indicator image of checkable QGroupBox for a check/uncheck states, #93
    - Fix the wrong comma position, #95
    - Added image for the missing QTreeView/QListView undetermined state, fix #92
- 2.5.3
    - Add future warning and pending deprecation for 3.0 version preparation #89
    - Add ISSUE\_TEMPLATE to ask for default information on the issue tracker
- 2.5.2:
    - Modularize files from example/ui to simplify edition (developers)
    - Add scripts to process files and run examples more easily (developers)
    - Better documentation (developers)
    - Add CONTRIBUTE, CODE\_OF\_CONDUCT, and PRODUCTION files
    - Lint markdown to standardize files
    - Fix and add more information in C++ example
- 2.5.1:
    - Fix Travis files, needs more improvement #74
    - Improve modules description
    - Update setup.py, remove the license
    - Update and improve README, CHANGES and AUTHORS
- 2.5:
    - Add a new complete example with new files
    - Add new screenshots for new example
    - Update Travis files
    - Add support to the example of QtPy and PyQtGraph
    - Move scripts for compiling to script folder
    - Update README, CHANGES
- 2.4:
    - Add function to get Qt information from environment variable #69, #70, #73
    - Add CC-BY license for images and transfer COPYING to LICENSE file #68
    - Fix tabs style - selected tab color and shift #59, #72
    - Restructure README creating AUTHORS, CHANGES, and LICENSE #71
- 2.3.1:
    - Improve checkbox color (use accent color used in other widgets) and
    darken view hover/selected colors to play nicer with other widget colors
    - Shift to the right of the first tab
    - Update license year
    - Update README (fix snapshots links and formatting)
    - Removed QLineEdit top/bottom padding which cut off a text while editing QListView items
- 2.3.0:
    - Add support for QDateEdit
- 2.2.2:
    - Add hover to the unselected item in QListView/QTreeView
    - Fixes for vertical QToolBar, QToolBar Extend Button & QTabWidget's Pane Misalignment
    - Fixed consistency of QTabBar depending on the position
- 2.2.1:
    - Remove border of status bar widgets
- 2.2:
    - Major update of the color scheme based on the Breeze Dark theme of KDE 5
    - Fix issues #29, #30, #31, #32 and #35
- 2.1:
    - Add style for QPushButton:checked
    - Improve QCheckBox and QRadioButton style
    - Add style for QMenu::right-arrow

- **2.0**:
    - Improve the stylesheet to make it look a bit more modern (see pull request #25)
- 1.16:
    - Fix QGroupBox title padding (see issue #20)
- 1.15:
    - Improve tristate checkbox graphics: the undetermined state is now represented by a dash
- 1.14:
    - Add support for tristate checkboxes and for vertical and horizontal lines
- 1.13:
    - Fix issue with horizontal scrollbar arrows, left and right were inversed.
- 1.12:
    - Fix the minimum size of input widgets (see issue #14)
- 1.11:
    - Fix QDockWidget title position on Mac.
    - Add QStatusBar support
    - Improve QToolButton especially the MenuButtonPopup and InstantPopup modes
- 1.10:
    - Add PyQt5 support
    - Fix bug #12 (dock widget title not dark on OSX. Note that this reopens issue #8 for MAC users)
- 1.9:
    - Improve QTabBar consistency and make selected tabs more distinctive
- 1.8:
    - Add support for QToolBox
    - Fix issue with grid line in QTableView if there is only ONE row/column
- 1.7:
    - Fix the appearance of bottom tab bars (invert gradient)
    - Improve QTableView: add grid line and fix section borders
    - Fix bug #7: bug when resizing QTableView
    - Fix bug #8: text validation not working on QDockWidget
- 1.6:
    - Improve QToolButton style
    - Add support for InstantPopup and MenuButtonPopup
    - Improve QMenu style (better spacing with icons)
    - Add \_\_version\_\_ to Python package.
- 1.5:
    - Improve QTabBar style: now works with all tab bar positions (North, South, West and East)
    - Fix bug #6: hide QTabBar base to avoid strange lines at the base of the tab bar.
- 1.4:
    - Add style.qss to qrc file, this fix issues with cx\_freeze
- 1.3:
    - Remove outline on button, checkbox and radio button
    - Add support for closable tabs
    - Better disabled buttons
    - Fix QTextEdit background color to match the color of QPlainTextEdit
    and QLineEdit
    - Better hover/selected states for QTreeView and QListView
    - Add QHeaderView support
- 1.2:
    - Improve QTableView support
- 1.1:
    - Switch to MIT license
    - Add python 3 support

- **1.0**:
    - First public release (LGPL v2)
