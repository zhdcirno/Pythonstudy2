import multiprocessing
from time import  ctime

def consumer(input_q):
    print("into consumer:", ctime())
    while True:
        # 处理
        item = input_q.get()
        print("pull", item, "out of q")# 此处替换为有用的工作
        input_q.task_done()# 发出信号通知完成
    print("qut of consumer:", ctime())# 未执行

def producer(sequence, output_q):
    print("into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of procuder:", ctime())

if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target= consumer, args= (q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)
    q.join()