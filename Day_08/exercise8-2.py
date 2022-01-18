# # Write your code below this line 👇
#
# def prime_checker(number):
#     if number % 2 == 0 and number !=2:
#         print('Not a prime number')
#     elif number % 3 == 0 and number !=3:
#         print('Not a prime number')
#     elif number % 5 == 0 and number !=5:
#         print('Not a prime number')
#     elif number % 7 == 0 and number !=7:
#         print('Not a prime number')
#     else:
#         print('Prime!')
#         return True
#
# prime = False
# while prime == False:
#     n = int(input("Check this number: "))
#     prime = prime_checker(number=n)
#
def prime_checker(number):
    is_prime=True
    for i in range(2, number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print('Its a prime number')
    else:
        print('not a prime number')
    return is_prime
is_prime=False
while is_prime == False:
    n = int(input("Check this number: "))
    is_prime = prime_checker(number=n)

