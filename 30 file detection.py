#checking to see whether a file exists or not

import os
path = "C:\\Users\\sange\\OneDrive\\Documents\\Python Scripts\\test.txt"
if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("That is a file!!!")
else:
    print("No such file!")

path_2 = "C:\\Users\\sange\\OneDrive\\Documents\\Python Scripts\\test folder"
if os.path.exists(path_2):
    print("The location exists!")
    if os.path.isfile(path_2):
        print("That is a file!!!")
    elif os.path.isdir(path_2):
        print("That is a directory!")
else:
    print("No such file/ directory!")
