# Smallest multiple
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?


def gcd(number1, number2):
    if number1 == 0:
        return number2
    else:
        return gcd(number2 % number1, number1)


def lcm(number1, number2):
    return int(number1 * number2 / gcd(number1, number2))


def find_product(max_number):
    product = 1
    for number in range(2, max_number+1):
        product = lcm(product, number)

    return product


print(find_product(20))
