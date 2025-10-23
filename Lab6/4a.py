import time
import math

n = int(input("number: "))
ms = int(input("milliseconds: "))

time.sleep(ms / 1000)
x = math.sqrt(n)

print("Square root of", n, "after", ms, "milliseconds is", x)
