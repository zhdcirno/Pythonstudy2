import time
import threading

def fun():
    print("start")
    time.sleep(2)
    print("end")

print("main thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)
print("main end")