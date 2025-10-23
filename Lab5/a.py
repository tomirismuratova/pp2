import re

txt = input(str())
s = re.sub(r"_", "15", txt)
print(s)