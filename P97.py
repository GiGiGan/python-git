import os
os.getcwd()
os.chdir("HeadFirstPython/chapter3")
os.getcwd()

data = open("sketch.txt")

for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':')
        print(role, end="")
        print("said:", end="")
        print(line_spoken, end="")

    data.close()
else:
    print('The data file is missing!')