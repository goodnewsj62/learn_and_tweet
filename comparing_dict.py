dict_a =  {"x": 1, "y":2, "z":11,"w":1}
dict_b =  {"x": 1,"f":2 , "z":11,"h":8}

print(dict_a.keys()) # prints a dict_keys([]) object
#RESULT: dict_keys(['x', 'y', 'z', 'w'])

print(dict_a.items())# print a dict_items([]) object
#RESULT: dict_items([('x', 1), ('y', 2), ('z', 11), ('w', 1)])

key_intesection = dict_a.keys() & dict_b.keys() 
# this perform an intesection of the keys, 
# the keys that exists in both dictionaries are printed
print(key_intesection)
# RESULT: {'x', 'z'}


items_intesection= dict_a.items() & dict_b.items()
#the above can also be done for the items of a dictionary d_items
# but this cant be done for values cause two keys can have same values
# as these are operations that can be carried on a set
print(items_intesection)
# RESULT: {('z', 11), ('x', 1)}


key_difference = dict_a.keys() - dict_b.keys()
print(key_difference) # print keys in dict_a  that is not in dict_b
#RESULT: {'w', 'y'}

union = dict_a.keys() | dict_b.keys()
print(union)
#RESULT: {'x', 'z', 'h', 'f', 'w', 'y'}
