print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_price = 0

if size == 'S':
    pizza_price = 15
    if add_pepperoni =='Y':
        pizza_price += 2
elif size == 'M':
    pizza_price = 20
    if add_pepperoni == 'Y':
        pizza_price += 3
elif size == 'L':
    pizza_price = 25
    if add_pepperoni == 'Y':
        pizza_price += 3
else:
    print('Input must be S, M or L')
if extra_cheese == 'Y':
    pizza_price += 1
print(f'Pizza price is ${pizza_price}')