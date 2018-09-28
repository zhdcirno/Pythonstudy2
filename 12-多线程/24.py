import multiprocessing
from time import  ctime

def consumer(input_q):
    print("into consumer:", ctime())
    while True:
        # 处理
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")# 此处替换为有用的工作

    print("qut of consumer:", ctime())# 未执行

def producer(sequence, output_q):
    print("into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of procuder:", ctime())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p1 = multiprocessing.Process(target= consumer, args= (q,))
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))

    cons_p1.start()
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()