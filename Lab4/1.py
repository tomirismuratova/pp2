def generator(N):
    for i in range(1, N + 1):
        yield i ** 2

for num in generator(5):
    print(num)

