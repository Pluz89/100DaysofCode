print('Welcome to the Leap Year Calculator')
year=int(input('Please put the year you wanna know '))

if year % 4 == 0:
    print('Divisible by 4')
    if year % 100 >= 1:
        print('Not divisible by 100')
        print(f'The year {year} is a Leap year, it has 366 days and is divisible by 4 but not by 100')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f'The year {year} is a Leap Year, it has 366 days and it is divisible by 400')
        else:
            print(f'The year {year} is not a Leap Year, it has 365 and it is divisible by 100')
else:
    print('Not divisible by 4')
    print(f'The year {year} is not a Leap Year, it has 365 days and it is not divisible by 4')