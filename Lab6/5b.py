list = ["Phone", "laptop", "ipad", "keyboard"]

with open("a.txt", "w") as f:
    for i in list:
        f.write(i + "\n")

print("Done")
