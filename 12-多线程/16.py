import  threading
import  time

# 参数定义最多几个线程同时使用
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + " get semaphero")
        time.sleep(5)
        semaphore.release()
        print(threading.currentThread().getName() + " release semaphero")

for i in range(7):
    t1 = threading.Thread(target=func())
    t1.start()