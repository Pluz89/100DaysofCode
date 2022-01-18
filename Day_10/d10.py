def format_name(input_fname, input_lname):
    """ Take the a first and last name and format it to return 
    the capitalized version of the name"""#---Docstring
    if input_fname=="" or input_lname=="":
        return 'You forgot the first name or last name'
    input_fname=input_fname.capitalize()
    input_lname=input_lname.capitalize()
    name=input_fname+' '+ input_lname
    return name
fname = input('Your first name: \n')
lname = input('Your last name: \n')


print(format_name(input_fname=fname, input_lname=lname))

#Docstrings: create a documentation while coding in function