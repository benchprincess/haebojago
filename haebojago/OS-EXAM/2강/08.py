# 내 파이썬 프로그램의 이름을 알아보자.
# 내 파이썬 프로그램이 돌아가면 그건 프로세스가 됨
# process는 import psutil을 이용해서 조회할 수 있음
# 내가 이용하고 있는 08.py와 동일한 프로세스를 발견하면 그 프로세스의 이름을 출력하는 코드 구현

import psutil
import os

def find_process(target):
    match_process = []
    print("현재 실행중인 프로세스 ID 목록")

    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            print(proc.info['pid'])

            if target in ' '.join(proc.info['cmdline']):
                match_process.append(proc.info['pid'])
        except:
            pass

    if match_process:
        print(f"08.py와 일치하는 프로세스: {', '.join(map(str, match_process))}")
    else:
        None

if __name__ == "__main__":
    find_process('08.py')