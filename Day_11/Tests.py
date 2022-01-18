# list=['a', 1, 'b', 2]
#
# def call_str(in_list):
#     for item_in_list in range(len(in_list)):
#         if 'a' == in_list[item_in_list] or 'b' == in_list[item_in_list]:
#             in_list[item_in_list] = 10
#             #in_list.pop(item_in_list)
#     return in_list
# list = call_str(in_list=list)
# print(list)
# def tryhit():
#     hit=True
#     while hit:
#         cancel=input('y to cancel n to continue')
#         if cancel=='y':
#             hit=False
#         elif cancel=='n':
#             print('continue')
# tryhit()
# lista = 8* [{'ace':1}, {'king':10}, {'2':2, '3':3}]
# print(lista[0]['ace'] + lista[1]['king'])

x=[20,19]
y=x
y.pop(0)
print(y)
y=x
print(y)
