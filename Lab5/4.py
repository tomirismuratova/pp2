import re

s = r'[A-Z][a-z]+'
t = input(str("Enter a string: "))
match = re.findall(s, t)

if match:
    print("Found:", match)
else:
    print("no match found")