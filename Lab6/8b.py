import os

path = input("path: ")

if os.path.exists(path):
    print("exists")

    if os.access(path, os.W_OK):
        os.remove(path)
        print("deleted")
    else:
        print("can not delete")
else:
    print("not exist")
