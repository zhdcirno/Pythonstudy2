# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.comm/jokerbj/p/7460260.html

# 多线程 vs 多进程
- 程序： 一堆代码以文本形式存入一个文档
- 进场： 程序运行的一个状态
    - 包含地址控件， 内存， 数据栈等
    - 每个进场由自己完全独立的运行环境，多线程共享数据是一个问题
- 线程
    - 一个进程的独立运行的片段，一个进程可以由多个线程
    - 轻量化的进程
    - 一个进程的多个线程共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - python代码的执行是由Python虚拟机进行控制
    - 在主循环中只能由一个控制线程在执行

- Python包
    - thread：python改成了_thread
    - threading:同行的包
    - 案例01:顺序执行，耗时长
    - 案例02：多线程执行,缩短总时间，使用_thread
    - 案例03：多线程，传参数

- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
    - 案例04
    - 案例05：加入join后的对比
    - 守护线程-daemon
        - 如果在线程中将子线程设置成保护线程，则子线程会在主线程结束时自动结束
        - 一般认为，守护线程不重要或者不允许离开主线程独立运行
        - 守护线程案例生效与否和环境有关
        - 案例06.07
    - 线程的常用属性
        - threading.currentThread: 返回当前线程变量
        - threading.enumerate：返回一个包含正在运行的线程的list
        - threading.activeCount：返回线程数量
        - thr.setName
        - thr.getName
        - 案例08
- 直接继承子threading.Thread
    - 直接继承Thread
    - 重写run函数
    - 可以直接运行
    - 案例09
    - 案例10 常用
- 共享变量
    - 共享变量：当多个线程同时访问一个变量的时候会出现问题
    - 案例11
    - 解决变量：锁，信号灯
    - 锁（lock）：
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源
            - 取消释放锁
        - 案例12
        - 锁谁： 哪个资源需要多个线程共享，锁谁
        - 锁是一个令牌
    - 线程安全问题：
        - 如果一个资源/变量，对于多线程讲，不加锁也没问题，则称为线程安全
        - 线程不安全变量类型： list，setdict
        - 线程安全变量类型： queue
    - 生产着消费着问题
        - 一个模型,可以用来搭建消息队列
        - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队（特殊list）
        - 案例13
    - 死锁问题
        - 案例14,15
    - semphore 006
        - 允许一个资源最多由几个多线程同时使用
        - 案例16
    - threading.Timer
        - 案例17
        - Timer 是利用多线程，在指定时间后启动一个功能
    - 可重入锁
        - 一个锁，可以倍一个线程多次申请
        - 主要解决递归调用的时候，需要申请锁的情况
        - 案例18

# 线程替代方案
    - subprocess
        - 完全跳过线程，使用继承
        - 是派生进程的主要替代方案
        - python2.4后引入
    - mutiprocessiong
        - 使用threading接口派生，使用子进程
        - 允许为多核或者多cpu派生进程，接口和threading相似
        - Python2.6
    - concurrent.futures
        - 新的异步执行模块
        - 任务级别的操作
        - Python3.2后

# 多进程
- 进程间通讯（InterprocessCommunication， IPC)
- 进程直接无共享
- 进程的创建
    - 直接生成Process实例对象，案例19
    - 派生对象，案例20
- 生产者消费者模型
    - JoinableQueue
    - 案例22
    - 队列中哨兵的使用，案例23
    - 哨兵的改进，案例24