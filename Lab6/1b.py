import os

path = input("path: ")

print("\nAll:", os.listdir(path))

print("\nDirectories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("\nFiles:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
