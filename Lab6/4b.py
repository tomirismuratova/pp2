f = input("file name: ")

with open(f, 'r') as f:
    lines = f.readlines()
    print("number of lines:", len(lines))
