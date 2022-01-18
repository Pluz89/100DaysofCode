counter=0
for counter in range(1, 101):
    if counter % 15 == 0:
        counter='FizzBuzz'
    elif counter % 5 == 0:
        counter='Buzz'
    elif counter % 3 == 0:
        counter='Fizz'
    print(counter)