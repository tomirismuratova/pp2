import time, math
n = int(input())
s = int(input())
time.sleep(s)
x = round(math.pow(n, 1/3))
print("Cube root of ",n ,"after", s, "seconds is", x)