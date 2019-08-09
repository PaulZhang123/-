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
import time
from openpyxl import load_workbook
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from samplesoftware import Ui_MainWindow
from cknowledgeTask import *
from readexcel import * 
from configTask import *
from textread import *

class mainTask(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainTask, self).__init__()
        self.setupUi(self)
        # 自定义窗口标题并只显示最小化按钮
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.CustomizeWindowHint)
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸,在show之前进行
        
        self.m_knowledge= None;
        #建立消息响应
        self.pushButton_qiangda.released.connect(self.onClickQuesionDlgQiangda)
        self.pushButton_fengxian.released.connect(self.onClickQuesionDlgFengxian)
        self.pushButton_lunda.released.connect(self.onClickQuesionDlgLunda)
        self.pushButton_shenmi.released.connect(self.onClickQuesionDlgShenmi)

        self.action_cfg.triggered.connect(self.showCfgDialog)
        self.action_transvoice.triggered.connect(self.transVoice)
        self.config = configTask()
        
    def onClickQuesionDlgQiangda(self):
        self.readexcel = readexcel(self.config.quespath)
        self.readexcel.readExcelQiangda()
        self.m_knowledge = cknowledgeTask(self.config.voiceEnable,self.config.countTime,self.config.local)
        self.m_knowledge.setQuestionList(self.readexcel.qiandaQuestionList,"randomMode")
        self.m_knowledge.show()
       

    def onClickQuesionDlgFengxian(self):
        self.readexcel = readexcel(self.config.quespath)
        self.readexcel.readExcelFengxian()
        self.m_knowledge = cknowledgeTask(self.config.voiceEnable,self.config.countTime,self.config.local)
        self.m_knowledge.setQuestionList(self.readexcel.fengxianQuestionList,"levelMode")
        self.m_knowledge.show()
        

    def onClickQuesionDlgLunda(self):
        self.readexcel = readexcel(self.config.quespath)
        self.readexcel.readExcellunda()
        self.m_knowledge = cknowledgeTask(self.config.voiceEnable,self.config.countTime,self.config.local)
        self.m_knowledge.setQuestionList(self.readexcel.lundaQuestionList,"sequenceMode")
        self.m_knowledge.show()

    def onClickQuesionDlgShenmi(self):
        self.readexcel = readexcel(self.config.quespath)
        self.readexcel.readExcelQiangda()
        self.readexcel.readExcelFengxian()
        self.readexcel.readExcellunda()
        shenmiList = self.readexcel.qiandaQuestionList+self.readexcel.fengxianQuestionList+self.readexcel.lundaQuestionList
        self.m_knowledge = cknowledgeTask(self.config.voiceEnable,self.config.countTime,self.config.local)
        self.m_knowledge.setQuestionList(shenmiList,"randomMode")
        self.m_knowledge.show()

    def showCfgDialog(self):
        self.config.show()

    def transVoice(self):
        #读取题目信息
        readExcel = readexcel(self.config.quespath)
        readExcel.readExcelQiangda()
        readExcel.readExcelFengxian()
        readExcel.readExcellunda()
        #转换为语音，保存到设备
        textread = textRead(True)
        for j in range(0,len(readExcel.qiandaQuestionList)):
            contentstr = readExcel.qiandaQuestionList[j]['content']
            contentstr = contentstr.replace("<br>","。")
            contentstr = re.sub("<img src=\'.+\'>", "", contentstr)
            textread.baiduread2(contentstr,unicode(".\\voice\\"+readExcel.qiandaQuestionList[j]['sheet']+readExcel.qiandaQuestionList[j]['cfgIdx']+"Q.mp3"))
            answerstr = readExcel.qiandaQuestionList[j]['answer']
            textread.baiduread2(answerstr,unicode(".\\voice\\"+readExcel.qiandaQuestionList[j]['sheet']+readExcel.qiandaQuestionList[j]['cfgIdx']+"A.mp3"))
        for j in range(0,len(readExcel.fengxianQuestionList)):
            contentstr = readExcel.fengxianQuestionList[j]['content']
            contentstr = contentstr.replace("<br>","。")
            contentstr = re.sub("<img src=\'.+\'>", "", contentstr)
            textread.baiduread2(contentstr,unicode(".\\voice\\"+readExcel.fengxianQuestionList[j]['sheet']+readExcel.fengxianQuestionList[j]['cfgIdx']+"Q.mp3"))
            answerstr = readExcel.fengxianQuestionList[j]['answer']
            textread.baiduread2(answerstr,unicode(".\\voice\\"+readExcel.fengxianQuestionList[j]['sheet']+readExcel.fengxianQuestionList[j]['cfgIdx']+"A.mp3"))
        for j in range(0,len(readExcel.lundaQuestionList)):
            contentstr = readExcel.lundaQuestionList[j]['content']
            contentstr = contentstr.replace("<br>","。")
            contentstr = re.sub("<img src=\'.+\'>", "", contentstr)
            textread.baiduread2(contentstr,unicode(".\\voice\\"+readExcel.lundaQuestionList[j]['sheet']+readExcel.lundaQuestionList[j]['cfgIdx']+"Q.mp3"))
            answerstr = readExcel.lundaQuestionList[j]['answer']
            textread.baiduread2(answerstr,unicode(".\\voice\\"+readExcel.lundaQuestionList[j]['sheet']+readExcel.lundaQuestionList[j]['cfgIdx']+"A.mp3")) 

        # print "transVoice has finished"

    def closeEvent(self, event):
        '''
        关闭工具
        '''
        reply = QtGui.QMessageBox.question(self, 'Notice', u'确定要关闭工具吗？', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            time.sleep(0.1)
            event.accept()
        else:
            event.ignore()
        
def main():
    '''
    运行主窗口程序
    '''
    app = QtGui.QApplication(sys.argv)
    myapp = mainTask()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
