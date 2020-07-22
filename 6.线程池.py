from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum

# 定义一个线程结束后就会执行的回调函数
def callback(f):
    print("线程"+threading.current_thread().name+"已结束")
    print(f.result())

# # 创建一个包含2条线程的线程池
# pool = ThreadPoolExecutor(max_workers=2)
# # 向线程池提交一个task, 50会作为action()函数的参数
# future1 = pool.submit(action, 50)
#
# # 向线程池再提交一个task, 100会作为action()函数的参数
# future2 = pool.submit(action, 100)
# # 判断future1代表的任务是否结束
# print(future1.done())
# # time.sleep(3)   #主线程阻塞
# # 判断future2代表的任务是否结束
# print(future2.done())
#
# # future1.add_done_callback(callback)
# # future2.add_done_callback(callback)
#
# #如果线程并未完成，则会阻塞主线程，直到该线程能够完成
# # 查看future1代表的任务返回的结果
# print("================================")
# print(future1.result())
# print("================================")
# # 查看future2代表的任务返回的结果
# print(future2.result())


with ThreadPoolExecutor(max_workers=4) as pool:
    results=pool.map(action,(5,10,20))
    print("=================")
    print(list(results))
