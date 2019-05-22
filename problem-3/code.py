NUMBER = 600851475143


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def factorization(number):
    factors = []
    for i in range(2, int(number/2)):
        if number == 1:
            break
        elif is_prime(i):
            while number % i == 0:
                number = number/i
                factors.append(i)

    return factors


print(factorization(NUMBER))
