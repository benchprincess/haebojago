import threading
from multiprocessing import Process, Value, Lock

def counter1(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        lock.release()

def counter2(snum, cnt, lock):
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        lock.release()

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 10000, lock))
    t1.start()

    t2 = threading.Thread(target=counter2, args=(shared_number, 10000, lock))
    t2.start()

    t1.join()
    t2.join()

    print("finally, number is", shared_number.value)