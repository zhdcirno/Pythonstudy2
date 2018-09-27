'''
利用time函数，生成两个函数
顺序调用
计算总运行时间
'''

import time
import _thread as thread

def loopl():
    print("s1", time.ctime())
    time.sleep(4)
    print("e1", time.ctime())

def loop2():
    print("s2", time.ctime())
    time.sleep(2)
    print("e2", time.ctime())

def main():
    print("sa", time.ctime())
    thread.start_new_thread(loopl, ())
    thread.start_new_thread(loop2, ())
    print("ea", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)