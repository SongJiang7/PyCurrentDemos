from threading import Thread
import threading

def action(*add):
    for arc in add:

        print(threading.current_thread().getName() +" "+ str(arc))

class Thread2(Thread):
    def __init__(self,p):
        Thread.__init__(self)
        self.param=p

    def run(self):
        for c in self.param:
            print(threading.current_thread().getName()+' '+str(c))

my_tuple1 = range(11,20)
my_tuple2 = range(10)
thread1 = Thread(target = action,args =my_tuple1)
thread2=Thread2(my_tuple2)
thread2.daemon=True



thread1.start()
thread2.start()



for i in range(5):
    print(threading.current_thread().getName())