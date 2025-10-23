import re

txt = input("Enter text: ")
x = re.findall(r'\d', txt)

print(x)
