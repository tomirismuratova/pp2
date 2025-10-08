from itertools import permutations

def func():
    s = input()
    perms = permutations(s)   
    for p in perms:
        print("".join(p))     

func()
