def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)
