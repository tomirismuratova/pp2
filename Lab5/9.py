import re

txt = input("string: ")

s = re.split(r'(?=[A-Z])', txt)
x = ' '.join(s)
print(x)
