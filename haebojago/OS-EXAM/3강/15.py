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
    p1 = Process(target=counter1, args=(shared_number, 5000, lock))
    p1.start()

    p2 = Process(target=counter2, args=(shared_number, 5000, lock))
    p2.start()

    p1.join()
    p2.join()

    print("finally, number is", shared_number.value)