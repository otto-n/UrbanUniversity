def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# результат подставится для именованных параметров, остальные выведутся по умолчанию
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['one', 2, True]
values_dict = {
    'a': 'four',
    'b': 5,
    'c': [1, 2, 3]
}
# передаем список в функцию для распаковки, как позиционные параметры функции
print_params(*values_list)
# передаем список в функцию для распаковки, как именованные параметры функции
print_params(**values_dict)

values_list_2 = [True, 'string']
# значения из списка подставятся функцию для "a" и "b"
print_params(*values_list_2, 42)