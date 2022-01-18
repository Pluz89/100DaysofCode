print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowern1 = name1.lower()
lowern2 = name2.lower()

nr_t = lowern1.count('t')+lowern2.count('t')
nr_r = lowern1.count('r')+lowern2.count('r')
nr_u = lowern1.count('u')+lowern2.count('u')
nr_e = lowern1.count('e')+lowern2.count('e')

true = nr_t + nr_r + nr_u + nr_e

nr_l = lowern1.count('l')+lowern2.count('l')
nr_o = lowern1.count('o')+lowern2.count('o')
nr_v = lowern1.count('v')+lowern2.count('v')
nr_e2 = lowern1.count('e')+lowern2.count('e')

love = nr_l + nr_o + nr_v + nr_e2

score_str = str(true) + str(love)
score_int = int(score_str)

if score_int <10 or score_int>90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
if score_int <50 and score_int>40:
    print(f"Your score is {score_int}, you are alright together.")
if score_int >= 10 and score_int <= 40 or score_int >=50 and score_int<=90:
    print(f'Your score is {score_int}.')