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
