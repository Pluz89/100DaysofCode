print('Welcome to Odd or Even')
nr = int(input('put your number'))
result = nr % 2
if result == 1:
    print('Your number is ODD')
elif result == 0:
    print('Your number is EVEN')