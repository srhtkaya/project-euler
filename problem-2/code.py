# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

MAX_VALUE = 4e6

# Legacy method

def fill_fibonacci(max_value):
    fib_list = [1, 1]
    increment = 1
    while(True):
        fib_list.append(fib_list[increment - 1] + fib_list[increment])
        increment = increment + 1
        if(fib_list[increment] > max_value):
            fib_list.pop()
            break
    return fib_list


print(sum([num for num in fill_fibonacci(MAX_VALUE) if num % 2 == 0]))

# With reactive programming

from rx import from_list, operators as op

source = from_list(fill_fibonacci(MAX_VALUE))
source.pipe(
    op.filter(lambda x : x %2==0),
    op.sum()
).subscribe(
    lambda i : print(i)
)
