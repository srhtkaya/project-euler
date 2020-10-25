# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythogorean_product(max_sum):
    for a in range(1, int(max_sum/2)):
        b = (1e6 - 2e3*a)/(2e3 - 2*a)

        if b > 0 and b.is_integer():
            c = 1e3 - a - b
            if(a + b + c == 1e3):
                return int(a*b*c)

print(pythogorean_product(1000))
