import re

txt = "My name is Tomiris, I'm 18"
x = re.sub(r"[ ,.]", ":", txt)
print(x)
