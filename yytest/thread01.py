#coding=utf-8
import time
import threading

def chi(people,do):
    print "%s 吃菜菜的同学%s"%(time.ctime(),people)
    time.sleep(3)
    for i in range(3):
        time.sleep(1)
        print "%s %s 正在%s 菜菜"%(time.ctime(),people,do)

    print "%s 吃菜菜的同学%s" % (time.ctime(), people)

class Mythread(threading.Thread):
    lock=threading.Lock()
    def __init__(self,people,name,do):
        threading.Thread.__init__(self)
        self.threadName=name
        self.people=people
        self.do=do
    def run(self):
        print "开始线程："+self.threadName
        self.lock.acquire()
        chi(self.people,self.do)
        self.lock.release()
        print  "结束线程："+self.name


print "开吃！！"
threads=[]
thread1=Mythread("zhangsan",'Thread-1','添加')
thread2=Mythread("lisi","Thread-2",'吃掉')
threads.append(thread1)
threads.append(thread2)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

time.sleep(1)
print "结束！！"




