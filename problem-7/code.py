# What is the 10 001st prime number?


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    primes = []
    i = 0
    while len(primes) < n+1:
        if is_prime(i):
            primes.append(i)
        i = i + 1
        continue
    return primes.pop()


print(nth_prime(10001))
