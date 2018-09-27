import threading

sum = 0
loopSun = 1000000

def myAdd():
    global sum, loopSun
    for i in range(1,loopSun):
        sum += 1

def muMinu():
    global sum, loopSun
    for i in range(1,loopSun):
        sum -= 1

if __name__ == '__main__':
    print("S{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=muMinu, args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("end...{0}".format(sum))