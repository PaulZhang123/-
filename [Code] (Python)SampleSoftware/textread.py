# coding:utf-8
import sys
from aip import AipSpeech
import mp3play
import time 
from datetime import datetime
import threading
reload(sys)
sys.setdefaultencoding('utf8')
'''
# __author__ = '郭 璞'
# __date__ = '2016/8/6'
# __Desc__ = 文字转语音输出
 

'''
mutex = threading.Lock()
class textRead():
    def __init__(self,enable=False):
        self.count_thread1 = 0
        self.enable = enable

    def slotStartText2Audio(self,context):
        if self.enable == True:
            #创建线程，并启用线程，调用线程中关联的模块方
            #创建线程，关联函数self.start_counting
            count_thread = threading.Thread(target=self.baiduread, args=[context])
            #设置守护线程
            count_thread.setDaemon(True)
            #设置线程名称
            count_thread.setName('count_thread')
            #启动线程
            count_thread.start()
            #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞
            #count_thread.join(timeout=None)
            
        
    def slotStartPlay(self,outputMp3,appendMp3):
        if self.enable == True:
            #创建线程，并启用线程，调用线程中关联的模块方
            #创建线程，关联函数self.start_counting
            
            if(self.count_thread1 != 0):
                while self.count_thread1.isAlive():
                    time.sleep(1)
                    print "self.count_thread1.isAlive:",self.count_thread1.isAlive()
            self.count_thread1 = threading.Thread(target=self.playAudio, args=[outputMp3,appendMp3])
            #设置守护线程
            self.count_thread1.setDaemon(True)
            #设置线程名称
            self.count_thread1.setName('count_thread1')
            #启动线程
            self.count_thread1.start()
            #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞
            #count_thread.join(timeout=None)
        
    def baiduread(self,context):
        mutex.acquire()
        outputMp3= '.\\audio.mp3'
        """ 你的 APPID AK SK """
        APP_ID = '14699088'
        API_KEY = 'FaSbGhmS0w9GmLO59cjCMT9m'
        SECRET_KEY = 'B4F8an3Iogp0pvIRViT0lC1pKLLPsT9C'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result  = client.synthesis(context, 'zh', 1, {
            'vol': 5,'per':0
        })
        print "start "
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(outputMp3, 'wb') as f:
                f.write(result) 
        mutex.release()

    def baiduread2(self,context,outputMp3):
        APP_ID = '14699088'
        API_KEY = 'FaSbGhmS0w9GmLO59cjCMT9m'
        SECRET_KEY = 'B4F8an3Iogp0pvIRViT0lC1pKLLPsT9C'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result  = client.synthesis(context, 'zh', 1, {
            'vol': 5,'per':0
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(outputMp3, 'wb') as f:
                f.write(result) 
    

    def pyttsxread(self,context):
        mutex.acquire()
        import pyttsx
        engine = pyttsx.init()
        volume = engine.getProperty('volume')
        print volume
        engine.setProperty('volume', volume+0.25)
        rate = engine.getProperty('rate')
        print rate
        engine.setProperty('rate', rate-50)
        engine.say(context)
        engine.runAndWait()
        mutex.release()

    def playAudio(self,outputMp3,appendMp3):
        mutex.acquire()
        print outputMp3
        clip = mp3play.load(appendMp3)
        clip.play()
        print clip.seconds()
        time.sleep(clip.seconds()+1)   
        clip.stop()
        clip = mp3play.load(outputMp3)
        clip.play()
        print clip.seconds()
        time.sleep(clip.seconds()+1)   
        clip.stop()
        mutex.release()

def main():
    '''
    运行主窗口程序
    '''
    myapp = textRead(True)
    test = ".\\voice\\fengxian1A.mp3"
    myapp.playAudio(test.decode("utf-8").encode("gbk"))
    time.sleep(5)


if __name__ == "__main__":
    main()

