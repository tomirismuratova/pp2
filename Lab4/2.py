a = []
def generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            a.append(str(i))
    yield ",".join(a)

n = int(input("Enter n: "))
for num in generator(n):
    print(num)
