# Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def find_products(digit):
    result = [0, 0, 0]
    max_number = 10**(digit)

    for i in range(10**(digit-1), max_number):
        for j in range(10**(digit-1), max_number):
            if(is_palindrome(i*j) and i*j > result[0]):
                result = [i*j, i, j]

    return result


print(find_products(3))
