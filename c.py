class Book:
    def __init__(self, author, name):
        self.author = author
        self.name = name
    def func(self):
        print(self.author, self.name)
a = Book("Jane Austin", "Flower")
a.func()

def unique(lst):
    u = []
    for i in lst:
        if i not in u:   
            u.append(i)
    return u

nums = [1, 2, 2, 3, 4, 4, 5]
print(unique(nums))  


from itertools import permutations

def func():
    s = input()
    perms = permutations(s)   
    for p in perms:
        print("".join(p))     

func()


def reverse_words():
    s = input()
    words = s.split()
    return " ".join(reversed(words))

print(reverse_words())

names = [
    {"name": "Aisha", "age" : 19},
    {"name": "Tomi", "age" : 20},
    {"name": "Arina", "age" : 18}
]
def func(names):
    for i in names:
        if i["age"] > 18:
            print(i["name"])
func(names)

class Myclass:
    def getString(self):
        return input()
    def printString(self, s):
        print(s.upper())

obj = Myclass()
a = obj.getString()  
obj.printString(a)