import re

s = r'a.*b$'
t = input(str("Enter s string: "))

if re.findall(s, t):
    print("Matched")
else:
    print("Not Matched")