# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_menus.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph.Qt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 231)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_71 = QtGui.QLabel(self.centralwidget)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.verticalLayout_4.addWidget(self.label_71)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuMenuSub = QtGui.QMenu(self.menuMenu)
        self.menuMenuSub.setObjectName(_fromUtf8("menuMenuSub"))
        self.menuMenuDelayed = QtGui.QMenu(self.menubar)
        self.menuMenuDelayed.setObjectName(_fromUtf8("menuMenuDelayed"))
        self.menuMenuSubDelayed = QtGui.QMenu(self.menuMenuDelayed)
        self.menuMenuSubDelayed.setObjectName(_fromUtf8("menuMenuSubDelayed"))
        self.menuMenuCheckale = QtGui.QMenu(self.menubar)
        self.menuMenuCheckale.setObjectName(_fromUtf8("menuMenuCheckale"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarDelayed = QtGui.QToolBar(MainWindow)
        self.toolBarDelayed.setObjectName(_fromUtf8("toolBarDelayed"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDelayed)
        self.toolBarCheckable = QtGui.QToolBar(MainWindow)
        self.toolBarCheckable.setObjectName(_fromUtf8("toolBarCheckable"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarCheckable)
        self.actionActionA = QtGui.QAction(MainWindow)
        self.actionActionA.setObjectName(_fromUtf8("actionActionA"))
        self.actionActionSubA = QtGui.QAction(MainWindow)
        self.actionActionSubA.setObjectName(_fromUtf8("actionActionSubA"))
        self.actionActionSubB = QtGui.QAction(MainWindow)
        self.actionActionSubB.setObjectName(_fromUtf8("actionActionSubB"))
        self.actionActionDelayedA = QtGui.QAction(MainWindow)
        self.actionActionDelayedA.setObjectName(_fromUtf8("actionActionDelayedA"))
        self.actionActionDelayedSubA = QtGui.QAction(MainWindow)
        self.actionActionDelayedSubA.setObjectName(_fromUtf8("actionActionDelayedSubA"))
        self.actionActionCheckableA = QtGui.QAction(MainWindow)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setObjectName(_fromUtf8("actionActionCheckableA"))
        self.actionActionCheckableSubAChecked = QtGui.QAction(MainWindow)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName(_fromUtf8("actionActionCheckableSubAChecked"))
        self.actionActionCheckableSubAUnchecked = QtGui.QAction(MainWindow)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName(_fromUtf8("actionActionCheckableSubAUnchecked"))
        self.menuMenuSub.addAction(self.actionActionSubA)
        self.menuMenuSub.addAction(self.actionActionSubB)
        self.menuMenu.addAction(self.actionActionA)
        self.menuMenu.addAction(self.menuMenuSub.menuAction())
        self.menuMenuSubDelayed.addAction(self.actionActionDelayedSubA)
        self.menuMenuDelayed.addAction(self.actionActionDelayedA)
        self.menuMenuDelayed.addAction(self.menuMenuSubDelayed.menuAction())
        self.menuMenuCheckale.addAction(self.actionActionCheckableA)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenuDelayed.menuAction())
        self.menubar.addAction(self.menuMenuCheckale.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionActionA)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionSubA)
        self.toolBar.addAction(self.actionActionSubB)
        self.toolBarDelayed.addAction(self.actionActionDelayedA)
        self.toolBarDelayed.addSeparator()
        self.toolBarDelayed.addAction(self.actionActionDelayedSubA)
        self.toolBarCheckable.addAction(self.actionActionCheckableA)
        self.toolBarCheckable.addSeparator()
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAChecked)
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAUnchecked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_71.setText(_translate("MainWindow", "Inside CentralWidget", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuMenuSub.setTitle(_translate("MainWindow", "Menu Sub", None))
        self.menuMenuDelayed.setTitle(_translate("MainWindow", "Menu Delayed", None))
        self.menuMenuSubDelayed.setTitle(_translate("MainWindow", "Menu Sub Delayed", None))
        self.menuMenuCheckale.setTitle(_translate("MainWindow", "Menu Checkable", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About QDarkStyle", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Tool bar actions", None))
        self.toolBarDelayed.setWindowTitle(_translate("MainWindow", "Tool bar actions delayed", None))
        self.toolBarCheckable.setWindowTitle(_translate("MainWindow", "Tool bar action checkable", None))
        self.actionActionA.setText(_translate("MainWindow", "Action A", None))
        self.actionActionSubA.setText(_translate("MainWindow", "Action A Sub", None))
        self.actionActionSubA.setToolTip(_translate("MainWindow", "Action A Sub", None))
        self.actionActionSubB.setText(_translate("MainWindow", "Action B Sub", None))
        self.actionActionDelayedA.setText(_translate("MainWindow", "Action Delayed A", None))
        self.actionActionDelayedA.setToolTip(_translate("MainWindow", "Action Delayed A", None))
        self.actionActionDelayedSubA.setText(_translate("MainWindow", "Action Delayed Sub A", None))
        self.actionActionDelayedSubA.setToolTip(_translate("MainWindow", "Action Delayed Sub A", None))
        self.actionActionCheckableA.setText(_translate("MainWindow", "Action Checkable A", None))
        self.actionActionCheckableA.setToolTip(_translate("MainWindow", "Action Checkable A", None))
        self.actionActionCheckableSubAChecked.setText(_translate("MainWindow", "Action Checkable Sub A Checked", None))
        self.actionActionCheckableSubAChecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Checked", None))
        self.actionActionCheckableSubAUnchecked.setText(_translate("MainWindow", "Action Checkable Sub A Unchecked", None))
        self.actionActionCheckableSubAUnchecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Unchecked", None))

