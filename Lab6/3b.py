import os

path = input("path: ")

if os.path.exists(path):
    print("exists")

    print("filename:", os.path.basename(path))

    print("directory:", os.path.dirname(path))
else:
    print("not exist")
