max_number = 1000
multiples = []

for number in range(max_number):
    if(number%3 == 0 or number%5 == 0):
        multiples.append(number)

print(sum(multiples))