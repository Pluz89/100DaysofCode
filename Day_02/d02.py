#Data types

#Important: Divisions show a result in FLOAT type
#           str() int() float() transform the value into the str int or float
#           You can use variable_name +=1 to sum 1 to the variable, same works with * / etc..
#           f'string = converts all str int float conveniently.

#Strings
'Hello'[4]

print('Hello'[0])#This will print the first character (0)
print('Hello'[4])

#Integers

print(123+456)
print(123_123_312)#Simple way to visualize numbers

#Float

print(type(3.14159))#Float

#Boolean

True
False
print(type(True))

#Convert to String:

num_char=len(input('What is your name? '))
new_num_char=str(num_char)
print('Your name has ' + new_num_char + ' characters')
print(type(new_num_char))
#Same is with float(), int(), bool()

3+5
7-4
3*2
#Divisions in python are float type
#POwer uses two **
2**3

# Math operator order=PEMDAS = Parenthesis, Exponent, Multiplication, Division, Addition and Substraction

#Floor division: print(8//3)= result is 2 in integer.