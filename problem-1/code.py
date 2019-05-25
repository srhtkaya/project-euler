# Find the sum of all the multiples of 3 or 5 below 1000.

from rx import from_list, operators as op
max_number = 1000

# Legacy method
multiples = []

for number in range(max_number):
    if(number % 3 == 0 or number % 5 == 0):
        multiples.append(number)

print(sum(multiples))

# With reactive programming
from_list(range(max_number)).pipe(
    op.filter(lambda n: n % 3 == 0 or n % 5 == 0),
    op.sum()
).subscribe(lambda s: print(s))
