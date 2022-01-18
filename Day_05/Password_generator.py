#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
################################
pwd_list=[]
print("Welcome to the Pablos Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for pick_letters in range(0, nr_letters):
    rng=random.randint(0, len(letters)-1)
    pwd_list.append(letters[rng])
nr_symbols = int(input(f"How many symbols would you like?\n"))
for pick_symbols in range(0, nr_symbols):
    rng=random.randint(0, len(symbols)-1)
    pwd_list.append(symbols[rng])
nr_numbers = int(input(f"How many numbers would you like?\n"))
for pick_numbers in range(0, nr_numbers):
    rng=random.randint(0, len(numbers)-1)
    pwd_list.append(numbers[rng])
random.shuffle(pwd_list)
password=''.join(pwd_list)
print(f'Your password {password} has been created')