# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

number = 100


def square_diff(n):
    sum_square = int((n*(n+1)/2)**2)
    square_sum = int(n*(n+1)*(2*n+1)/6)
    return sum_square - square_sum


print(square_diff(number))
