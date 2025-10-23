import os

path = input("path: ")

exists = os.path.exists(path)
print("exists:", exists)

print("readable:", os.access(path, os.R_OK))
print("writable:", os.access(path, os.W_OK))
print("executable:", os.access(path, os.X_OK))

if exists:
    if os.path.isfile(path):
        print("file")
    elif os.path.isdir(path):
        print("directory")
    else:
        print("other")
