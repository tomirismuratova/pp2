def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
                   
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

primes = list(filter(lambda x: is_prime(x), nums))
#filter берёт каждое число x из списка nums и вызывает is_prime(x) и здесь x передаётся как n

print(primes)
