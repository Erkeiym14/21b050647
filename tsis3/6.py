def isPrime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = [int(i) for i in input().split()]
numbers = range(n[-1])
print(list(filter(lambda n: isPrime(n), numbers)))