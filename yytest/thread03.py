#coding=utf-8
import threading,time

event=threading.Event()
def chi(name):
    print '%s %s 已经启动'%(time.ctime(),threading.currentThread().getName())
    event.wait()
    print '%s 准备就绪'%name
    time.sleep(1)

    print '%s 收到通知'%threading.currentThread().getName()
    print '%s 开吃'%name

#threads=[]
thread1=threading.Thread(target=chi,args=('a',))
thread2=threading.Thread(target=chi,args=('b',))
# threads.append(thread1)
# threads.append(thread2)
# for thread in threads:
#     thread.start()
thread1.start()
thread2.start()

time.sleep(0.2)
print '下发通知'
event.set()