# #Making a dictionary
# my_dictionary = {
#     'Bug': 'An insect',
#     123: 'q12o',
#     12.32: 23.23,
# }
# #Retrieving items from dictionary, msut be the same name
# print(my_dictionary[123])
# #adding new items
# my_dictionary['Bog'] = 'Not a bug'
# #Putting the same name will replace the item before
#
# print(my_dictionary['Bog'])
#
# #Create empty dictionary
# empty_dictionary = {}
# #Wipe an existing dictionary
# my_dictionary={}
# print(my_dictionary)
# #Edit in a dictionary
# my_new_dictionary = {
#     'Fly': 'Ugly',
#     12223: 932,
#     12.3332: 23.23,
# }
#
# my_new_dictionary['Bug'] = 'Cute fucking creature'
# #Loop through dictionary
# for key in my_new_dictionary:
#     print(key)
#     print(my_new_dictionary[key])
# #Nesting, you can nest a list inside a dictionary with a dictionary
nested_dictionary_and_lists={
    'Lista':[1, 2, 3, 4],
    'Diccionario':{'Hoho', 'haha'},
    'France':{'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12, },
    'Sweden':{'cities_visited':['Borlange', 'Stockholm', 'Kiruna'], 'items_bought': 92},

}

nested_dictionary_inside_a_list=[{
    'country': 'France',
    'cities_visited': ['Paris', 'Lyon', 'Marsella'],
    'total_visits': 12
},
{
    'country': 'Germany',
    'cities_visited': ['Dusseldorf', 'Frankfurt', 'Colonia'],
    'total_visits': 12

}]

print(nested_dictionary_inside_a_list[0])
list1=[1,2,3,[4,5,6]]