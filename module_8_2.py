from itertools import count


def personal_sum(numbers):
    result = incorrect_data = amount_ints = 0
    try:
        for n in numbers:
            result += n
            amount_ints += 1
    except TypeError:
        incorrect_data += 1

    return({'result' : result,
            'amount_ints' : amount_ints,
            'incorrect_data': incorrect_data})

def calculate_average(numbers):

    _summ = personal_sum(numbers)['result']

    try:
        return _summ / personal_sum(numbers)['amount_ints']
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'

print(f'Результат 1: {calculate_average("1, 2, 3")}') # числовой результат останется - 0, количество чисел 0
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Сумма - 4, а количество чисел 2
print(f'Результат 3: {calculate_average(567)}') # числовой результат останется - 0, количество чисел 0
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # найдет среднее арифметическое