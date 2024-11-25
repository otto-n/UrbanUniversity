my_dict = {'Maks': 1988, 'Dima': 1990, 'Igor': 1980}

print(my_dict)
print(my_dict['Igor'])
print(my_dict.get('Ivan', 'Значения по такому ключу в словаре не найдено'))

my_dict.update({'Ivan': 1530,
                'Petr': 1672})

forgot = my_dict.pop('Ivan')
print('Иван Грозный родился в ' + str(forgot) + ' г., но словарь этого уже не помнит')

print(my_dict)


my_set = {True, 'Brick', 77, False, True, 'Black', 'Brick', 77, 0}

print(my_set)
my_set.add(8)
my_set.add(9)
my_set.discard(True)
print(my_set)