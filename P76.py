import os
os.getcwd()
os.chdir("HeadFirstPython/chapter3")
os.getcwd()

data = open("sketch.txt")
print(data.readline(), end="")
print(data.readline(), end="")

data.seek(0)

for eacht_line in data:
    print(eacht_line, end="")

data.close()
