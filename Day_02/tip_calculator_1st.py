print('Welcome to the TIP calculator')
cost=float(input('Please put the cost of the total bill \n$'))
people=float(input('How many people will split the bill?\n'))
tip=float(input('How much percentage do you want to leave as tip?\n'))
cost_per_person=cost*(1+(tip/100))/people
rcost_per_person=round(cost_per_person,2)
rcost_per_person='{:.2f}'.format(cost_per_person)
print(f'The amount that each person has to pay is ${rcost_per_person}')

