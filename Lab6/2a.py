txt = input(str("string: "))

upp = sum(1 for i in txt if i.isupper())
low = sum(1 for i in txt if i.islower())

print("upper case letters:", upp)
print("lower case letters:", low)

