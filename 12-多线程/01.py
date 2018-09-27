'''
利用time函数，生成两个函数
顺序调用
计算总运行时间
'''

import time

def loopl():
    print(time.ctime())
    time.sleep(4)
    print(time.ctime())

def loop2():
    print(time.ctime())
    time.sleep(2)
    print(time.ctime())

def main():
    print(time.ctime())
    loopl()
    loop2()
    print(time.ctime())

if __name__ == '__main__':
    main()