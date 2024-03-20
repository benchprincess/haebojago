# 경로와 확장장자를 이용해 파일을 찾고, 내용을 읽기

import os
def searchFile(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            searchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, "r", encoding="utf-8") as f:
                    print(f.read())

searchFile("/Users/jiwon/Desktop/oz/benchprincess/haebojago/OS-EXAM", ".js")