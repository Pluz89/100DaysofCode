import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcoome to the Rock Paper Scisorrs Game..')
p_choice=int(input('Type 0 for Rock, 1 for Paper and 2 for Scissors: '))
cpu_choice=random.randint(0,2)

if p_choice == 0:
    print('Your choice is: ROCK', rock)
    if cpu_choice == 0:
        print(rock, 'CPU chooses ROCK')
        print('it\'s a DRAW!')
    elif cpu_choice == 1:
        print(paper, 'CPU chooses PAPER')
        print('You LOSE!')
    elif cpu_choice == 2:
        print(scissors, 'CPU chooses SCISSORS')
        print('You WIN!')

if p_choice == 1:
    print('Your choice is: PAPER', paper)
    if cpu_choice == 0:
        print(rock, 'CPU chooses ROCK')
        print('You WIN!')
    elif cpu_choice == 1:
        print(paper, 'CPU chooses PAPER')
        print('it\'s a DRAW!')
    elif cpu_choice == 2:
        print(scissors, 'CPU chooses SCISSORS')
        print('You LOSE!')

if p_choice == 2:
    print('Your choice is: SCISSORS', scissors)
    if cpu_choice == 0:
        print(rock, 'CPU chooses ROCK')
        print('You LOSE!')
    elif cpu_choice == 1:
        print(paper, 'CPU chooses PAPER')
        print('You WIN!')
    elif cpu_choice == 2:
        print(scissors, 'CPU chooses SCISSORS')
        print('it\'s a DRAW!')


#Write your code below this line 👇
