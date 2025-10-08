def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))  

nums = list(map(int, input().split()))
print("prime numbers:", filter_prime(nums))