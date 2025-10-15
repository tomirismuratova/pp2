import re

s = r'ab{2,3}'

text = input("Enter a string: ")

if re.fullmatch(s, text):
    print("Matched!")
else:
    print("Not matched!")
