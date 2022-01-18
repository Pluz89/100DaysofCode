# import random
# # import mymodule
# # print(mymodule.pi)
# random_integer = random.randint(1,10)
# print(random_integer)
# #random number from 0.0000 to 0.99999
# random_float = random.random()
# print(random_float)
# ex=random_float*5
# print(ex)
# love_score=random.randint(1,100)
# print('Your love score is: ', love_score)
# # exercise = random.uniform(0,5)
# # print(exercise)

state1='Delaware'
state2='Pensylvania'
states_of_america = ['Delaware', 'Pennsylvania', 'Philadelphia']
print(states_of_america[1])
print(states_of_america[-1])#Gets the last item in the list

#You can alter the list:
states_of_america[0] = 'DEEEELAWARE'
print(states_of_america)
#You can also add to the list if you wanted. To add an  Item at the end of the list:
states_of_america.append('PAbloLand')
print(states_of_america)
states_of_america.extend(['Potopelao', 'FUckasssss'])#Adds a bunch of items at the end of the list
print(states_of_america)
num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])

list1=['Mesa', 'Silla', 'Lapices']
list2=['Gatos', 'Perros', 'Caballos']
mix=[list1, list2]
print(mix)