# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_views.ui'
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(266, 387)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_70 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.gridLayout.addWidget(self.label_70, 0, 1, 1, 1)
        self.label_80 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.gridLayout.addWidget(self.label_80, 0, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 1, 0, 1, 1)
        self.listView = QtGui.QListView(self.dockWidgetContents)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 1, 1, 1)
        self.listViewDis = QtGui.QListView(self.dockWidgetContents)
        self.listViewDis.setEnabled(False)
        self.listViewDis.setObjectName(_fromUtf8("listViewDis"))
        self.gridLayout.addWidget(self.listViewDis, 1, 2, 1, 1)
        self.label_59 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout.addWidget(self.label_59, 2, 0, 1, 1)
        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 2, 1, 1, 1)
        self.treeViewDis = QtGui.QTreeView(self.dockWidgetContents)
        self.treeViewDis.setEnabled(False)
        self.treeViewDis.setObjectName(_fromUtf8("treeViewDis"))
        self.gridLayout.addWidget(self.treeViewDis, 2, 2, 1, 1)
        self.label_60 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout.addWidget(self.label_60, 3, 0, 1, 1)
        self.tableView = QtGui.QTableView(self.dockWidgetContents)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 3, 1, 1, 1)
        self.tableViewDis = QtGui.QTableView(self.dockWidgetContents)
        self.tableViewDis.setEnabled(False)
        self.tableViewDis.setObjectName(_fromUtf8("tableViewDis"))
        self.gridLayout.addWidget(self.tableViewDis, 3, 2, 1, 1)
        self.label_61 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout.addWidget(self.label_61, 4, 0, 1, 1)
        self.columnView = QtGui.QColumnView(self.dockWidgetContents)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout.addWidget(self.columnView, 4, 1, 1, 1)
        self.columnViewDis = QtGui.QColumnView(self.dockWidgetContents)
        self.columnViewDis.setEnabled(False)
        self.columnViewDis.setObjectName(_fromUtf8("columnViewDis"))
        self.gridLayout.addWidget(self.columnViewDis, 4, 2, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Views", None))
        self.label_70.setText(_translate("DockWidget", "Enabled", None))
        self.label_80.setText(_translate("DockWidget", "Disabled", None))
        self.label_27.setText(_translate("DockWidget", "ListView", None))
        self.label_59.setText(_translate("DockWidget", "TreeView", None))
        self.label_60.setText(_translate("DockWidget", "TableView", None))
        self.label_61.setText(_translate("DockWidget", "ColunmView", None))

