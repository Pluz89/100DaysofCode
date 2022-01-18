#HANGMAN
#Step 1
import random
game_over=False
lives=6
result=0
word_list = ["aardvark", "baboon", "camel", "pencil", "dog", "sound", 'duck', 'alessandria']

aux=random.randint(0, len(word_list)-1)
chosen_word=word_list[aux]
print(f'Pss... chosen word is {chosen_word}')
display = list(chosen_word)
list_chosen_word= list(chosen_word)

for n in range(len(chosen_word)):
    display[n]='_'

while game_over != True:
    print(display)
    guess = input('Choose a letter to make a guess.\n')
    guess = guess.lower()

    #Check for the letter
    for n in range(len(chosen_word)):
        if guess == chosen_word[n]:
            result+=1
            display[n]=chosen_word[n]
        #elif guess != chosen_word[n]:
         #  result=False
    print(f'{result} letters correct!')
    result=0
    #Wrong result
    if guess not in chosen_word:
        print('Wrong! You lost a life')
        lives-=1
        print(f'You have {lives} left!')
    #Game Over Conditions
    if list_chosen_word == display:
        game_over=True
    if lives == 0:
        print('You Loooooooooooooooooose. GAME OVER')
        game_over=True

print(display)