my_dict = {'Max': 1988, 'Andrey': 1969, 'Olga': 1970, 'Larisa': 1950}
print('Dict:', my_dict)
print('Existing value:', my_dict['Andrey'])
print('Not existing value:', my_dict.get('Alena'))
my_dict.update({'Nikolay': 1989,
                'Yuriy': 1959})
p_name = my_dict.pop('Olga')
print('Deleted value:', p_name)
print('Modified dictionary:', my_dict)
print('')

my_set = {1, 2, 5, 4, 1, 3, 3.333, 6, 4, 1, 'Game', (5, 4, 3), 'Cube', 'Game', False}
print('Set:', my_set)
my_set.add(89)
my_set.add('Python')
my_set.remove((5, 4, 3))
print('Modified set:', my_set)