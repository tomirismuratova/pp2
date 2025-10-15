import re

s = r'ab*'

text = input("Enter a string: ")

if re.fullmatch(s, text):
    print("Matched!")
else:
    print("Not matched!")
