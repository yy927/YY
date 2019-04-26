#coding=utf-8
import threading
import time
con=threading.Condition()
num=0

class Producter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global num
        con.acquire()
        while True:
            print "开始添加"
            num +=1
            print "个数:%s"%num
            time.sleep(0.5)
            if num>=2:
                print "最多了，无法添加"
                con.notify() #唤醒等待的线程
                con.wait()
        con.release()
class Customer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while True:
            print "开吃"
            num-=1
            print "剩余个数:%s" % num
            if num<=0:
                print "请添加"
                con.notify()
                con.wait()
        con.release()

p=Producter()
c=Customer()

p.start()
c.start()
