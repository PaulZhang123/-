# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Important\code\(Python)SampleSoftware\cknowledge.ui'
#
# Created: Wed Nov 14 15:47:48 2018
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

class Ui_CKnowledge(object):
    def setupUi(self, CKnowledge):
        CKnowledge.setObjectName(_fromUtf8("CKnowledge"))
        CKnowledge.setWindowModality(QtCore.Qt.ApplicationModal)
        CKnowledge.setEnabled(True)
        CKnowledge.resize(1216, 875)
        CKnowledge.setAutoFillBackground(False)
        CKnowledge.setStyleSheet(_fromUtf8("background-color: rgb(218, 215, 199);"))
        self.formLayout = QtGui.QFormLayout(CKnowledge)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.widget = QtGui.QWidget(CKnowledge)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(_fromUtf8("border-image: url(:/img/img/yangpi.png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.label_leftQsCnt = QtGui.QLabel(self.widget)
        self.label_leftQsCnt.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label_leftQsCnt.setObjectName(_fromUtf8("label_leftQsCnt"))
        self.horizontalLayout_2.addWidget(self.label_leftQsCnt)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 10, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.label_No = QtGui.QLabel(self.widget)
        self.label_No.setAutoFillBackground(False)
        self.label_No.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label_No.setObjectName(_fromUtf8("label_No"))
        self.gridLayout.addWidget(self.label_No, 3, 9, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 12, 1, 3)
        self.label_No_2 = QtGui.QLabel(self.widget)
        self.label_No_2.setAutoFillBackground(False)
        self.label_No_2.setStyleSheet(_fromUtf8("font: 36pt \"微软雅黑\";"))
        self.label_No_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_No_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_No_2.setObjectName(_fromUtf8("label_No_2"))
        self.gridLayout.addWidget(self.label_No_2, 2, 3, 1, 11)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 10, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 8, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 12, 1, 3)
        self.textEdit_answer = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit_answer.sizePolicy().hasHeightForWidth())
        self.textEdit_answer.setSizePolicy(sizePolicy)
        self.textEdit_answer.setAutoFillBackground(False)
        self.textEdit_answer.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.textEdit_answer.setObjectName(_fromUtf8("textEdit_answer"))
        self.gridLayout.addWidget(self.textEdit_answer, 8, 3, 1, 9)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 8, 14, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 10, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 10, 3, 1, 1)
        self.label_timer = QtGui.QLabel(self.widget)
        self.label_timer.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 48pt \"Academy Engraved LET\";"))
        self.label_timer.setText(_fromUtf8(""))
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setObjectName(_fromUtf8("label_timer"))
        self.gridLayout.addWidget(self.label_timer, 10, 5, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 10, 11, 1, 2)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 10, 13, 1, 2)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 9, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 6, 15, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 8, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 11, 5, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 8, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 6, 16, 1, 1)
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.pushButton_Test = QtGui.QPushButton(self.widget)
        self.pushButton_Test.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
"border-color: rgb(255, 234, 180);"))
        self.pushButton_Test.setObjectName(_fromUtf8("pushButton_Test"))
        self.horizontalLayout1.addWidget(self.pushButton_Test)
        self.pushButton_timer = QtGui.QPushButton(self.widget)
        self.pushButton_timer.setAutoFillBackground(False)
        self.pushButton_timer.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
"border-color: rgb(255, 234, 180);"))
        self.pushButton_timer.setObjectName(_fromUtf8("pushButton_timer"))
        self.horizontalLayout1.addWidget(self.pushButton_timer)
        self.pushButton_showAnswer = QtGui.QPushButton(self.widget)
        self.pushButton_showAnswer.setAutoFillBackground(False)
        self.pushButton_showAnswer.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
"border-color: rgb(255, 234, 180);"))
        self.pushButton_showAnswer.setObjectName(_fromUtf8("pushButton_showAnswer"))
        self.horizontalLayout1.addWidget(self.pushButton_showAnswer)
        self.pushButton_Next = QtGui.QPushButton(self.widget)
        self.pushButton_Next.setAutoFillBackground(False)
        self.pushButton_Next.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
"border-color: rgb(255, 234, 180);"))
        self.pushButton_Next.setObjectName(_fromUtf8("pushButton_Next"))
        self.horizontalLayout1.addWidget(self.pushButton_Next)
        self.gridLayout.addLayout(self.horizontalLayout1, 10, 6, 1, 5)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 7, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 2, 2, 1)
        self.textEdit_question = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textEdit_question.sizePolicy().hasHeightForWidth())
        self.textEdit_question.setSizePolicy(sizePolicy)
        self.textEdit_question.setAutoFillBackground(False)
        self.textEdit_question.setStyleSheet(_fromUtf8("font: 26pt \"微软雅黑\";"))
        self.textEdit_question.setObjectName(_fromUtf8("textEdit_question"))
        self.gridLayout.addWidget(self.textEdit_question, 5, 3, 1, 9)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget)

        self.retranslateUi(CKnowledge)
        QtCore.QMetaObject.connectSlotsByName(CKnowledge)

    def retranslateUi(self, CKnowledge):
        CKnowledge.setWindowTitle(_translate("CKnowledge", "SampleSoftware", None))
        self.label.setText(_translate("CKnowledge", "剩余题数：", None))
        self.label_leftQsCnt.setText(_translate("CKnowledge", "1", None))
        self.label_No.setText(_translate("CKnowledge", "1", None))
        self.label_No_2.setText(_translate("CKnowledge", "传输显示知识竞赛", None))
        self.label_4.setText(_translate("CKnowledge", "答案：", None))
        self.label_2.setText(_translate("CKnowledge", "当前题号：", None))
        self.textEdit_answer.setHtml(_translate("CKnowledge", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_Test.setText(_translate("CKnowledge", "TEST", None))
        self.pushButton_timer.setText(_translate("CKnowledge", "开始计时", None))
        self.pushButton_showAnswer.setText(_translate("CKnowledge", "显示答案", None))
        self.pushButton_Next.setText(_translate("CKnowledge", "下一题", None))
        self.label_3.setText(_translate("CKnowledge", "问题：", None))
        self.textEdit_question.setHtml(_translate("CKnowledge", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import samplesoftware_rc
