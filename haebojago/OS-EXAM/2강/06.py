from multiprocessing import Process
import os
import time

def func():
    print('안녕, 나는 실험용으로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디:', os.getpid())
    print('나의 부모 프로세스 아이디:', os.getpid())

if __name__ =="__main__":
    print('05.py 프로세스 아이디', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=func)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=func)
    child3.start()
    time.sleep(0.5)