# Largest palindrome product


def is_palindrome(number):
    string_num = str(number)
    reversed_num = string_num[::-1]
    if reversed_num == string_num:
        return True
    return False


def find_products(digit):
    products = []
    max_number = 10**(digit)

    for i in range(10**(digit-1), max_number):
        for j in range(10**(digit-1), max_number):
            if(is_palindrome(i*j)):
                products.append([i*j, i, j])
            else:
                continue

    return products


print(max(find_products(3)))
