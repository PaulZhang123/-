# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Important\svn\PJ20181121113219261\trunk\(Python)SampleSoftware\samplesoftware.ui'
#
# Created: Tue Dec 04 11:52:10 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(684, 445)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("border-image:url(:/img/img/yangpi.png)"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_shenmi = QtGui.QPushButton(self.centralwidget)
        self.pushButton_shenmi.setGeometry(QtCore.QRect(390, 240, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.pushButton_shenmi.setFont(font)
        self.pushButton_shenmi.setObjectName(_fromUtf8("pushButton_shenmi"))
        self.pushButton_fengxian = QtGui.QPushButton(self.centralwidget)
        self.pushButton_fengxian.setGeometry(QtCore.QRect(390, 100, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.pushButton_fengxian.setFont(font)
        self.pushButton_fengxian.setObjectName(_fromUtf8("pushButton_fengxian"))
        self.pushButton_lunda = QtGui.QPushButton(self.centralwidget)
        self.pushButton_lunda.setGeometry(QtCore.QRect(110, 240, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.pushButton_lunda.setFont(font)
        self.pushButton_lunda.setObjectName(_fromUtf8("pushButton_lunda"))
        self.pushButton_qiangda = QtGui.QPushButton(self.centralwidget)
        self.pushButton_qiangda.setGeometry(QtCore.QRect(110, 100, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.pushButton_qiangda.setFont(font)
        self.pushButton_qiangda.setObjectName(_fromUtf8("pushButton_qiangda"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.action_cfg = QtGui.QAction(MainWindow)
        self.action_cfg.setObjectName(_fromUtf8("action_cfg"))
        self.action_help = QtGui.QAction(MainWindow)
        self.action_help.setObjectName(_fromUtf8("action_help"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_transvoice = QtGui.QAction(MainWindow)
        self.action_transvoice.setObjectName(_fromUtf8("action_transvoice"))
        self.menu.addAction(self.action_cfg)
        self.menu.addAction(self.action_transvoice)
        self.menu_2.addAction(self.action_help)
        self.menu_2.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "抽题软件", None))
        self.pushButton_shenmi.setText(_translate("MainWindow", "神秘题", None))
        self.pushButton_fengxian.setText(_translate("MainWindow", "风险题", None))
        self.pushButton_lunda.setText(_translate("MainWindow", "轮答题", None))
        self.pushButton_qiangda.setText(_translate("MainWindow", "抢答题", None))
        self.menu.setTitle(_translate("MainWindow", "配置", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))
        self.action_cfg.setText(_translate("MainWindow", "配置", None))
        self.action_help.setText(_translate("MainWindow", "帮助文档", None))
        self.action_about.setText(_translate("MainWindow", "关于", None))
        self.action_transvoice.setText(_translate("MainWindow", "转换语音", None))

import samplesoftware_rc
