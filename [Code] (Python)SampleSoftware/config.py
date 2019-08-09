# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Important\svn\PJ20181121113219261\trunk\(Python)SampleSoftware\config.ui'
#
# Created: Tue Dec 04 13:43:33 2018
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(382, 158)
        self.pushButton_save = QtGui.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 100))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.lineEdit_time = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_time.setObjectName(_fromUtf8("lineEdit_time"))
        self.gridLayout.addWidget(self.lineEdit_time, 2, 2, 1, 1)
        self.lineEdit_quespath = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_quespath.setObjectName(_fromUtf8("lineEdit_quespath"))
        self.gridLayout.addWidget(self.lineEdit_quespath, 3, 2, 1, 4)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.comboBox_enable = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_enable.setObjectName(_fromUtf8("comboBox_enable"))
        self.comboBox_enable.addItem(_fromUtf8(""))
        self.comboBox_enable.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_enable, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboBox_enable_2 = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_enable_2.setObjectName(_fromUtf8("comboBox_enable_2"))
        self.comboBox_enable_2.addItem(_fromUtf8(""))
        self.comboBox_enable_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_enable_2, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_save.setText(_translate("Dialog", " 保存", None))
        self.lineEdit_time.setText(_translate("Dialog", "10", None))
        self.lineEdit_quespath.setText(_translate("Dialog", ".\\question.xlsx", None))
        self.label_4.setText(_translate("Dialog", "秒", None))
        self.label.setText(_translate("Dialog", "语音功能：", None))
        self.label_3.setText(_translate("Dialog", "倒计时：", None))
        self.label_2.setText(_translate("Dialog", "题库路径：", None))
        self.comboBox_enable.setItemText(0, _translate("Dialog", "启用", None))
        self.comboBox_enable.setItemText(1, _translate("Dialog", "禁用", None))
        self.label_5.setText(_translate("Dialog", "本地语音：", None))
        self.comboBox_enable_2.setItemText(0, _translate("Dialog", "启用", None))
        self.comboBox_enable_2.setItemText(1, _translate("Dialog", "禁用", None))

