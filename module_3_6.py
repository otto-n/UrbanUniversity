def calculate_structure_sum(data, counter=0):
    if isinstance(data, int):  # Если число, добавляем к счетчику
        return counter + data

    if isinstance(data, str):  # Если строка, добавляем её длину
        return counter + len(data)

    if isinstance(data, (list, tuple, set)):  # Если список, кортеж или множество
        for item in data:
            counter = calculate_structure_sum(item, counter)
        return counter

    if isinstance(data, dict):  # Если словарь, обрабатываем ключи и значения
        for key, value in data.items():
            counter = calculate_structure_sum(key, counter)
            counter = calculate_structure_sum(value, counter)
        return counter

    return counter  # Если тип данных не подходит, возвращаем текущий счётчик


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)