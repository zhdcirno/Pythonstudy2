import time
import _thread as thread

def loop1(in1):
    print("s1", time.ctime())
    print("我是参数", in1)
    time.sleep(4)
    print("e1", time.ctime())

def loop2():
    print("s2", time.ctime())
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print("e2", time.ctime())

def main():
    print("sa", time.ctime())
    thread.start_new_thread(loop1, ("第一", ))
    thread.start_new_thread(loop2, ("第二", "第三"))
    print("ea", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)