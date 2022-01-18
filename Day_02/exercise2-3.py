print('Welcome to the exercise that will make you feel DEPRESSED!')
days_90yo = 365*90
weeks_90yo = 52*90
months_90yo = 12*90
age = int(input('Please input your current age\n'))

age_in_days = age*365
age_in_weeks = age*52
age_in_months = age*12

dleft = days_90yo - age_in_days
wleft = weeks_90yo - age_in_weeks
mleft = months_90yo - age_in_months

print(f'You have {dleft} days, {wleft} weeks and {mleft} months until you hit 90 years old')


