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


class configFile():
    def __init__(self):
        self.cfgFile = ".\\cfg.txt"
       
    def saveCfg(self,logmsg):
        f= open(self.cfgFile,'a+')
        f.write(logmsg+"\n")
        f.close

    def readCfg(self,mode):
        quesIdxList = []
        f= open(self.cfgFile,'a+')
        try:
            for line in f.readlines():
                line = line.strip('\n')
                partLines = line.split(":")
                if partLines[0]==mode:
                    quesIdxList.append(partLines[1])
        finally:
            f.close
            print quesIdxList
            return quesIdxList


