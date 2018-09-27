import  threading
import  time


lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print("函数1开始")
    lock_1.acquire(timeout=4)
    print("1申请到了")
    time.sleep(2)
    print("1等待")

    rst = lock_2.acquire(timeout=2)
    if rst:
        print("1已经得到锁")
        lock_2.release()
        print("1释放")
    else:
        print("1没申请到")

    lock_1.release()
    print("1释放了")
    print("1 done")


def func_2():
    print("函数2开始")
    lock_2.acquire()
    print("2申请到了")
    time.sleep(4)
    print("2等待")

    lock_1.release()
    print("2释放了1")
    lock_2.release()
    print("2释放了2")

    print("2 done")

if __name__ == '__main__':
    print("主程序启动啦")
    t1 = threading.Thread(target=func_1(), args=())
    t2 = threading.Thread(target=func_2(), args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束啦")