import re

txt = input("string: ")

s = re.split(r'(?=[A-Z])', txt)

print(s)
