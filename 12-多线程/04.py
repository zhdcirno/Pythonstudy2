import time
import threading

def loop1(in1):
    print("s1", time.ctime())
    print("我是参数", in1)
    time.sleep(4)
    print("e1", time.ctime())

def loop2(in1,in2):
    print("s2", time.ctime())
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print("e2", time.ctime())

def main():
    print("sa", time.ctime())
    t1 = threading.Thread(target=loop1, args=("第一", ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("第二", "第三"))
    t2.start()
    print("ea", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
