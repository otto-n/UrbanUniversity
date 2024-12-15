data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Эта рекурсивная функция преобразовывает все данные в список
# если элемент списка это число, то прибавляет его к счетчику
# если элемент списка это строка, то прибавляет к счетчику кол-во символов в строке
# по умолчанию счетчик равен нулю, но этот параметр обновляется, если среди элементов списка найдено число или строка
def calculate_structure_sum(data_, counter = 0):

    # Если входные данные это не пустой список
    if isinstance(data_, list) and len(data_) > 0:
        # Если первый элемент списка это не строка и не число
        if not isinstance(data_[0], str) and not isinstance(data_[0], int):
            # Если это словарь
            if isinstance(data_[0], dict):
                # Достаем элемент и записываем в переменную (удаляя из списка)
                element_ = data_.pop(0)
                # Преобразовываем элемент в тип данных - список
                element_ = list(element_.items())
                # Закидываем элемент в конец основного списка.
                data_.append(element_)
                # Рекурсивно вызываем функцию. Важно передавать счетчик даже если с ним не было никаких манипуляций
                # т.к. по умолчанию счетчик обнуляется.
                return calculate_structure_sum(data_, counter)
            # Для кортежа аналогично.
            elif isinstance(data_[0], tuple):
                element_ = data_.pop(0)
                element_ = list(element_)
                data_.append(element_)
                return calculate_structure_sum(data_, counter)
            # Для множества аналогично.
            elif isinstance(data_[0], set):
                element_ = data_.pop(0)
                element_ = list(element_)
                data_.append(element_)
                return calculate_structure_sum(data_, counter)
            # Если элемент списка это список
            elif isinstance(data_[0], list):
                # Проверяем, чтобы он был не пустой
                if len(data_[0]) > 0:
                    # Аналогично предыдущим
                    element_ = data_[0].pop(0)
                    data_.append(element_)
                # Если пустой ликвидируем его.
                else: data_.pop(0)
                return calculate_structure_sum(data_, counter)
        # Если элементом списка оказалась строка
        elif isinstance(data_[0], str):
            # Прибавляем к счетчику число равное кол-ву символов строки
            counter += len(data_[0])
            # Удаляем строку из списка
            data_.pop(0)
            return calculate_structure_sum(data_, counter)
        # С числом аналогично предыдущему.
        elif isinstance(data_[0], int):
            counter += data_[0]
            data_.pop(0)
            return calculate_structure_sum(data_, counter)

    # возвращаем счетчик, когда список данных опустошится
    return counter

result = calculate_structure_sum(data_structure)
print(result)