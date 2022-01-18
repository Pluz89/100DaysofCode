print('Welcome to the BMI Calculator!')
weight=float(input('Please submit your weight in kg\n'))
height=float(input('Please submit your height in m\n'))
BMI=weight/(height**2)
rBMI=round(BMI,0)
print(f'Your BMI is {rBMI} and the meaning shows below')
if BMI < 18.5:
    print('You are UNDERWEIGHT!')
elif BMI <=25:
    print('Your weight is NORMAL')
elif BMI <=30:
    print('Your are OVERWEIGHT')
elif BMI <39:
    print('Your are OBESE')
else:
    print('You are EXTREMELY OBESE!!')
