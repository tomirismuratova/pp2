import re

txt = input("snake_case string: ")

s = txt.split('_')
camel_case = s[0] + ''.join(i.capitalize() for i in s[1:])

print("Camel case:", camel_case)
