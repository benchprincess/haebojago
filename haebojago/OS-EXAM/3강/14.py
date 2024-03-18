from multiprocessing import Process, Value

def counter1(snum, cnt):
    for i in range(cnt):
        snum.value += 1

def counter2(snum, cnt):
    for i in range(cnt):
        snum.value -= 1

if __name__ == "__main__":

    shared_number = Value('i', 0)
    p1 = Process(target=counter1, args=(shared_number, 5000))
    p1.start()

    p2 = Process(target=counter2, args=(shared_number, 5000))
    p1.start()

    p1.join()
    p2.join()

    print("finally, number is", shared_number.value)