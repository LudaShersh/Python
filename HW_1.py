item_string = 'Luda'
item_integer = 26
item_float = 26.4
item_bytes = b'Hello everyone'
item_list = [1, item_string, 9.6, [item_integer, 'age'], True]
item_tuple = ('Art', 27, False)
item_set = {'Magro', 25, True}
item_frozenset = frozenset({'Margo', 25, True})
item_dict = {'name' : 'Luda', 'second name' : 'Hanchar', 'age' : 26}

print('type =', type(item_string), ',', 'item_string =', item_string)
print('type =', type(item_integer), ',', 'item_integer =', item_integer)
print('type =', type(item_float), ',', 'item_float =', item_float)
print('type =', type(item_bytes), ',', 'item_bytes =', item_bytes)
print('type =', type(item_list), ',', 'item_list =', item_list)
print('type =', type(item_tuple), ',', 'item_tuple =', item_tuple)
print('type =', type(item_set), ',', 'item_set =', item_set)
print('type =', type(item_frozenset), ',', 'item_frozenset =', item_frozenset)
print('type =', type(item_dict), ',', 'item_dict =', item_dict)

first_name = 'Luda'
second_name = 'Hanchar'
print('full name = ' + first_name + ' ' + second_name)

print(item_string, ',', item_integer)
print(item_string, '+', item_integer)