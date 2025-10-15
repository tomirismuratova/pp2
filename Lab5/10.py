import re

txt = input("camel_case str: ")

s = re.split(r'(?=[A-Z])', txt)
x = '_'.join(s).lower()

print("snake case:", x)
