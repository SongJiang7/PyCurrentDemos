import threading
import time
class A:
    def __init__(self):
        self.lock = threading.RLock()
    def foo(self, b):
        try:
            self.lock.acquire()
            print("当前线程名: " + threading.current_thread().name\
                + " 进入了A实例的foo()方法" )     # ①
            time.sleep(0.2)
            print("当前线程名: " + threading.current_thread().name\
                + " 企图调用B实例的last()方法")   # ③
            b.last()
        finally:
            self.lock.release()
    def last(self):
        try:
            self.lock.acquire()
            print("进入了A类的last()方法内部")
        finally:
            self.lock.release()
class B:
    def __init__(self):
        self.lock = threading.RLock()
    def bar(self, a):
        try:
            self.lock.acquire()
            print("当前线程名: " + threading.current_thread().name\
                + " 进入了B实例的bar()方法" )   # ②
            time.sleep(0.2)
            print("当前线程名: " + threading.current_thread().name\
                + " 企图调用A实例的last()方法")  # ④
            a.last()
        finally:
            self.lock.release()
    def last(self):
        try:
            self.lock.acquire()
            print("进入了B类的last()方法内部")
        finally:
            self.lock.release()
a = A()
b = B()
def init():
    threading.current_thread().name = "主线程"
    # 调用a对象的foo()方法
    a.foo(b)
    print("进入了主线程之后")
def action():
    threading.current_thread().name = "副线程"
    # 调用b对象的bar()方法
    b.bar(a)
    print("进入了副线程之后")
# 以action为target启动新线程
threading.Thread(target=action).start()
# 调用init()函数
init()