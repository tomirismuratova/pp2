def unique(lst):
    u = []
    for i in lst:
        if i not in u:   
            u.append(i)
    return u

nums = [1, 2, 2, 3, 4, 4, 5]
print(unique(nums))  
