<<<<<<< HEAD
import threading
import time
class mythread(threading.Thread):
    def __init__(self,Threadname):
        self.name = Threadname
        threading.Thread.__init__(self,name = threadname)
    def run(self):
        for i in range(10):
            print(self.getName,i)
            time.sleep(1)
t1 = mythread('t1')
print(t1.getName(),t1.isDaemon())
t1.setDaemon(True)
print(t1.getName(),t1.isDaemon())
t1.start()
print('main thread exit')
=======
from threading import Thread
import subprocess
from queue import Queue

num_threads = 3
ips = ['192.168.1.108','192.168.1.101','127.0.0.1']
q = Queue()
def pingit(i,queue):
    while True:
        ip = Queue.get()
        print('thread %s is pinging %s' % (i,ip))
        ret = subprocess.call('ping -c 3 %s' % ip,shell = True,stdout=open('/dev/null','w'))
        if ret != 0:
            print('%s is down' % ip)
        Queue.task_done()
for i in range(num_threads):
    t = Thread(target=pingit,args=(i,q))
    t.setDaemon(True)
    t.start()
for ip in ips:
    q.put(ip)
print('main thread is waiting...')
q.join()
print('done...')
>>>>>>> b1bc931f55b9e3256a52a06c5c990c9c0b323bad
