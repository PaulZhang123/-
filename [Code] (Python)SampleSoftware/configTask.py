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
from config import Ui_Dialog
from PyQt4.QtCore import QThread, SIGNAL
class configTask(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        super(configTask, self).__init__()
        self.setupUi(self)
        # 自定义窗口标题并只显示最小化按钮
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸,在show之前进行
        #建立消息响应
        self.pushButton_save.released.connect(self.onClickSave)
   
        self.quespath = ".\question.xlsx"
        self.voiceEnable = True
        self.local = True
        self.countTime = 10
        self.lineEdit_quespath.setText(self.quespath)
       
    def onClickSave(self):
        self.quespath = self.lineEdit_quespath.text()
        self.quespath= unicode(self.quespath.toUtf8(),'utf-8','ignore')
        if self.comboBox_enable.currentText() == u'启用':
            self.voiceEnable = True
        else:
            self.voiceEnable = False
        if self.comboBox_enable_2.currentText() == u'启用':
            self.local = True
        else:
            self.local = False
        self.countTime = int(unicode(self.lineEdit_time.text(),'utf-8','ignore'))
        print "voiceEnable:",self.voiceEnable
        print "local:",self.local
        QtGui.QMessageBox.information(self, u'提示', u'设置成功')

def main():
    '''
    运行主窗口程序
    '''
    app = QtGui.QApplication(sys.argv)
    myapp = configTask()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
