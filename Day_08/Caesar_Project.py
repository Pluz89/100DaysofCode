alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_textlist=[]
wrong_answer=True
#CAESAR
def caesar(enc_dec, plain_text, shift_amount):
    #Check if its encode /decode
    if enc_dec == 'decode':
        shift_amount *= -1
    #Start reading text
    for letter in range(len(plain_text)):
        if plain_text[letter] not in alphabet:
            cipher_textlist.append(plain_text[letter])
        if plain_text[letter] in alphabet:
            cipher_nrlist=alphabet.index(plain_text[letter])+shift_amount
            if cipher_nrlist >=26:
                cipher_nrlist-=26
            cipher_textlist.append(alphabet[cipher_nrlist])
        cipher_text = ''.join(cipher_textlist)
    print(f'The text is {cipher_text}.')
#Input direction with wrong checker
while wrong_answer == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        wrong_answer=False
wrong_answer=True
#Input text with wrong checker
# while wrong_answer == True:
text = input("Type your message:\n").lower()
print('Processing word... OK to go.')
#Shift
shift = int(input("Type the shift number:\n"))

caesar(enc_dec=direction, plain_text=text, shift_amount=shift)
