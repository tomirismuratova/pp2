with open("original.txt", "r") as f1:
    cnt = f1.read()         

with open("copy.txt", "w") as f2:
    f2.write(cnt)                

print("Done!")
