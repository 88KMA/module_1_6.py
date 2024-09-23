my_dict = {'Max': 1988, 'Andrey': 1969, 'Olga': 1970, 'Larisa': 1950}
print(my_dict)
print(my_dict['Andrey'])
my_dict['Alena'] = 1998
print(my_dict['Alena'])
my_dict.update({'Nikolay': 1989,
                'Yuriy': 1959})
p_name = my_dict.pop('Olga')
print(p_name)
print(my_dict)
print('')

my_set = {1, 2, 5, 4, 1, 3, 6, 4, 1, 'Game', (5, 4, 3), 'Cube', 'Game', False}
print(my_set)
my_set.add(89)
my_set.add('Python')
my_set.remove((5, 4, 3))
print(my_set)