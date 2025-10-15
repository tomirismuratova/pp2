import re

x = r'^[a-z]+_[a-z]+$'
t = input(str("Ebter a string: "))

if re.fullmatch(x, t):
    print("Matched")
else:
    print("Not Matched")