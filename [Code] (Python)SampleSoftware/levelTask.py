#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# -----------------------------------------------------------------------------
# Purpose:    远程测试分辨率客户端（应用于传输显示产品测试）
# Author:      lianjiaxin
# Created:     2017-09-25
# Copyright:   (c) Hikvision.com 2016
# -----------------------------------------------------------------------------
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from PyQt4 import QtCore, QtGui
from level import Ui_Dialog
from PyQt4.QtCore import QThread, SIGNAL
class levelTask(QtGui.QDialog, Ui_Dialog):
    def __init__(self,parent):
        super(levelTask, self).__init__()
        self.setupUi(self)
        # 自定义窗口标题并只显示最小化按钮
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸,在show之前进行
        self.widget.setStyleSheet(("QGroupBox{color:white};QPushButton{color:black}"))
        #建立消息响应
        self.pushButton_high.released.connect(self.onClickQuesionHigh)
        self.pushButton_middle.released.connect(self.onClickQuesionMiddle)
        self.pushButton_low.released.connect(self.onClickQuesionLow)

        self.pushButton_culture.released.connect(self.onClickQuesionCultrue)
        self.pushButton_sport.released.connect(self.onClickQuesionSport)
        self.pushButton_history.released.connect(self.onClickQuesionHistory)
        self.pushButton_entertain.released.connect(self.onClickQuesionEntertain)
        self.pushButton_geo.released.connect(self.onClickQuesionGeo)
        self.pushButton_life.released.connect(self.onClickQuesionLife)
        self.pushButton_sure.released.connect(self.onClickSure)
        self.pushButton_cancel.released.connect(self.onClickCancel)
        self.btnStyle = "QPushButton{color:black}QPushButton:hover{color:red}QPushButton{background-color:lightgreen}"
        self.hardLevel = ""
        self.subject = ""

        self.connect(self,QtCore.SIGNAL("sendmsg(QString, QString)"),parent.dealLevel)

    def onClickQuesionHigh(self):
        self.pushButton_middle.setStyleSheet("")
        self.pushButton_low.setStyleSheet("")
        self.pushButton_high.setStyleSheet(self.btnStyle)
        self.hardLevel = "3"
    def onClickQuesionMiddle(self):
        self.pushButton_middle.setStyleSheet(self.btnStyle)
        self.pushButton_low.setStyleSheet("")
        self.pushButton_high.setStyleSheet("")
        self.hardLevel = "2"

    def onClickQuesionLow(self):
        self.pushButton_middle.setStyleSheet("")
        self.pushButton_low.setStyleSheet(self.btnStyle)
        self.pushButton_high.setStyleSheet("")
        self.hardLevel = "1"

    def resetButton(self):
        self.pushButton_culture.setStyleSheet("")
        self.pushButton_sport.setStyleSheet("")
        self.pushButton_history.setStyleSheet("")
        self.pushButton_entertain.setStyleSheet("")
        self.pushButton_geo.setStyleSheet("")
        self.pushButton_life.setStyleSheet("")

    def onClickQuesionCultrue(self):
        self.resetButton()
        self.pushButton_culture.setStyleSheet(self.btnStyle)
        self.subject = u"文化"

    def onClickQuesionSport(self):
        self.resetButton()
        self.pushButton_sport.setStyleSheet(self.btnStyle)
        self.subject = u"体育"

    def onClickQuesionHistory(self):
        self.resetButton()
        self.pushButton_history.setStyleSheet(self.btnStyle)
        self.subject = u"历史"

    def onClickQuesionEntertain(self):
        self.resetButton()
        self.pushButton_entertain.setStyleSheet(self.btnStyle)
        self.subject = u"娱乐"

    def onClickQuesionGeo(self):
        self.resetButton()
        self.pushButton_geo.setStyleSheet(self.btnStyle)
        self.subject = u"地理"

    def onClickQuesionLife(self):
        self.resetButton()
        self.pushButton_life.setStyleSheet(self.btnStyle)
        self.subject = u"生活"

    def onClickSure(self):
        #将信号发送给类
        self.emit(QtCore.SIGNAL("sendmsg(QString,QString)"),self.hardLevel,self.subject)
        #关闭对话框
        self.emit(QtCore.SIGNAL("close()"))

    def onClickCancel(self):
        self.resetButton()
        self.pushButton_middle.setStyleSheet("")
        self.pushButton_low.setStyleSheet("")
        self.pushButton_high.setStyleSheet("")
        self.subject = ""
        self.hardLevel = ""

def main():
    '''
    运行主窗口程序
    '''
    app = QtGui.QApplication(sys.argv)
    myapp = levelTask()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
