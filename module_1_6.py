my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Masha'])
my_dict['Masha'] = 2000
print(my_dict['Masha'])
my_dict['Masha'] = 2002
my_dict.update({'Artem': 1915, 'Kamila': 1981})
del my_dict['Egor']
print(my_dict.get('Egor'))
my_set = {1, 'Яблоко', 42.314,1, 'Яблоко', 42.314}
print(my_set)
my_set.update([13,(5,6,1.6)])
print(my_set)
my_set.remove(1)
print(my_set)