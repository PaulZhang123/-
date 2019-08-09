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
from cknowledge import Ui_CKnowledge
from level import Ui_Dialog
from textread import *
import random
import threading
from levelTask import *
from configFile import *
import re
class cknowledgeTask(QtGui.QWidget, Ui_CKnowledge):
    """
    远程访问服务端PC，并获取和设置服务端的分辨率参数（vesa）.
    """
    def __init__(self,voiceEnable=False,countTime=10,local=False):
        super(cknowledgeTask, self).__init__()
        self.setupUi(self)
        # 自定义窗口标题并只显示最小化按钮
        self.textEdit_question.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.textEdit_answer.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_leftQsCnt.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_2.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_3.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_4.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_No.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_No_2.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.label_timer.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.pushButton_timer.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.pushButton_showAnswer.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.pushButton_Next.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.pushButton_Test.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);


        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.CustomizeWindowHint)
        #self.setFixedSize(self.width(), self.height())  # 禁止拉伸,在show之前进行
        self.textEdit_question.setText(QtCore.QString(unicode("（示例）现在计算机类产品发布一般以什么方式庆祝祈祷？\nA.发奖金\nB.砸电脑\nC.杀人\n")))
        self.textEdit_answer.setText("")
        self.labelIdx = 0
        self.answerFlag = True
        self.m_knowledge= None
        self.quesIdx = -1
        self.timeCnt = 0
        self.timer = None
        #建立消息响应
        #self.pushButton.triggered.connect(self.onClickQuesionDlg)
        self.pushButton_timer.released.connect(self.onClickBeginTimer)
        self.pushButton_showAnswer.released.connect(self.onClickShowAnswer)
        self.pushButton_Next.released.connect(self.onClickNextQuestion)
        self.pushButton_Test.released.connect(self.onClickTest)

        self.textread = textRead(voiceEnable)
        self.configFile = configFile()
        self.countTime = countTime
        self.local = local;

    def setQuestionList(self,questionList,chooseMode):
        self.questionList = questionList
        self.chooseMode = chooseMode

    def onClickBeginTimer(self):
        #开始计时
        self.pushButton_timer.setEnabled(False)
        self.timeCnt=self.countTime
        self.label_timer.setText(QtCore.QString(unicode(str(self.timeCnt))))
        self.timer = threading.Timer(1.0, self.updateLabel, [])
        self.timer.start()

        return 
    def updateLabel(self):
        self.timeCnt -= 1
        self.label_timer.setText(QtCore.QString(unicode(str(self.timeCnt))))
        if(0 == self.timeCnt):
            self.label_timer.setText("")
            self.timer.cancel()
            self.pushButton_timer.setEnabled(True)
        else:
            self.timer = threading.Timer(1.0, self.updateLabel, [])
            self.timer.start()

    def onClickShowAnswer(self):
        self.answerFlag = True
        '''
        QList<QVariant> rowData
        if (m_timer.isActive())
        {
            m_timer->stop()
            self.label_timer->setText("")
        }
        '''
        #self.textread.slotStartPlay(".\\answer.mp3")
        #显示答案
        print "self.quesIdx:",self.quesIdx
        if (self.quesIdx < len(self.questionList) and self.quesIdx>=0):
            rowData = self.questionList[self.quesIdx]
            print rowData['answer']
            answerstr = str(rowData['answer'])
            self.textEdit_answer.setText(QtCore.QString(unicode(answerstr)))
            #qsDb->writeCfg(rowData['idx'])
            self.configFile.saveCfg(self.questionList[self.quesIdx]['sheet']+":"+self.questionList[self.quesIdx]['cfgIdx'])
           
            if self.local == False:
                self.textread.slotStartText2Audio(answerstr)
                self.textread.slotStartPlay(".\\audio.mp3",".\\answer.mp3")
            else:
                voiceStr = ".\\voice\\"+self.questionList[self.quesIdx]['sheet']+self.questionList[self.quesIdx]['cfgIdx']+"A.mp3"
                voiceStr = voiceStr.decode("utf-8").encode("gbk")
                self.textread.slotStartPlay(voiceStr,".\\answer.mp3")

            del self.questionList[self.quesIdx]
            self.quesIdx = -2

        elif (-1 == self.quesIdx):
            self.textEdit_answer.setText(QtCore.QString(unicode("C")))

        return

    def onClickNextQuestion(self):
        if (0 == len(self.questionList)):
            QtGui.QMessageBox.information(self, u'提示', u'已到最后一题!!!!')
            return 

        if (False == self.answerFlag):
            QtGui.QMessageBox.information(self, u'提示', u'请显示答案!!!!')
            return 

        if 'randomMode' == self.chooseMode:
            #随机抽取模式
            self.quesIdx = random.randint(1,len(self.questionList)) -1
            self.showNextQues()
        elif 'sequenceMode' == self.chooseMode:
            #顺序抽取模式
            self.quesIdx = 0
            self.showNextQues()
        elif 'levelMode' == self.chooseMode:
            #类别抽取模式
            self.levelDlg = levelTask(self)
            self.levelDlg.show()
        else:
            print "error Mode"
       
        return

    def onClickTest(self):
        if (False == self.answerFlag):
            QtGui.QMessageBox.information(self, u'提示', u'请显示答案!!!!')
            return
        self.textEdit_question.setText(QtCore.QString(unicode("（示例）现在计算机类产品发布一般以什么方式庆祝祈祷？\nA.发奖金\nB.砸电脑\nC.杀人\n")))
        self.textEdit_answer.setText("")
        self.quesIdx = -1

    def showNextQues(self):
        #QtGui.QMessageBox.information(self, u'提示', str(self.quesIdx))
        self.answerFlag = False
        
        #显示下一题内容
        self.labelIdx = self.labelIdx+1
        self.label_No.setText(QtCore.QString(str(self.labelIdx)))
        rowData = self.questionList[self.quesIdx]
        
        contentstr = str(rowData['content'])
        self.textEdit_question.setText("")
        self.textEdit_question.insertHtml(QtCore.QString(unicode(contentstr))); 
        #self.textread.slotStartPlay(".\\listen.mp3")
        if self.local == False:
            contentstr = contentstr.replace("<br>","。")
            contentstr = re.sub("<img src=\'.+\'>", "", contentstr)
            self.textread.slotStartText2Audio(contentstr)
            self.textread.slotStartPlay(".\\audio.mp3",".\\listen.mp3")
        else:
            voiceStr = ".\\voice\\"+self.questionList[self.quesIdx]['sheet']+self.questionList[self.quesIdx]['cfgIdx']+"Q.mp3"
            voiceStr = voiceStr.decode("utf-8").encode("gbk")
            self.textread.slotStartPlay(voiceStr,".\\listen.mp3")

        self.textEdit_answer.setText(QtCore.QString(""))
        self.label_leftQsCnt.setText(QtCore.QString(str(len(self.questionList)-1)))

        

    def dealLevel(self,levelMsg,subMsg):
        #QtGui.QMessageBox.information(self, u'提示', levelMsg+subMsg)
        #根据标签选择
        for x in xrange(0,len(self.questionList)):
            print levelMsg,self.questionList[x]['level'],subMsg,self.questionList[x]['subject']
            if levelMsg == self.questionList[x]['level'] and subMsg==self.questionList[x]['subject']:
                #QtGui.QMessageBox.information(self, u'提示', self.questionList[x]['content'])
                self.quesIdx = x
                self.levelDlg.hide()
                self.showNextQues()
                return 
        QtGui.QMessageBox.information(self, u'提示', u"库中已无符合条件题目")
def main():
    '''
    运行主窗口程序
    '''
    app = QtGui.QApplication(sys.argv)
    myapp = cknowledgeTask()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


   