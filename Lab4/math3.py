import math

n = int(input("Number of sides: "))
l= int(input("Length of a side: "))
S = (n * l**2) / (4 * math.tan(math.pi / n))
print("S =", int(S))
