# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma, example: Pablo, Benja...\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

rnd_num=random.randint(0, len(names)-1)
print(rnd_num)
print(f'{names[rnd_num]} is going to buy the meal today!')
