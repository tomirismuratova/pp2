def func(s):
    cnt = 0
    for i in s:
        if i.isalpha():
            cnt += 1
    return cnt
      
a = "abscd142"
print(func(a)) 
