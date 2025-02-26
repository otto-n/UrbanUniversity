import random

# Функция получает значение в виде целого числа от 3 до 20, если число в функцию не передано
# тогда число создается рандомно
def get_passnumber(number = random.randint(3,20)):

    print('Вычисляем пароль для числа:', number)

    # Создаем пустой список в него будем записывать вычисленные пары
    two_stone = []

    # Запускаем вложенные циклы.
    # Во внешнем перебираем первое слогаемое от 1 до размера передаваемого числа
    for i in range(1, number + 1):

        # Во внутреннем цикле перебираем второе слогаемое от 2 до размера передаваемого числа
        for j in range(2, number + 1):

            # Если переданное число делится на сумму подбираемых чисел без остатка, значит оно соотвествует (кратно)
            # смотрим нет ли этих чисел уже в списке в обратном порядке, 3 2 - 2 3 например
            # а также проверяем не повторяются ли пары, 2 2 например
            if (number % (i + j) == 0) and not [j, i] in two_stone and i != j:

                # Добавляем в конец списка, как результат
                two_stone.append([i, j])

    # Прерываем выполнение функции, возвращаем результат
    return two_stone

print('Результат вычисления функции с рандомным числом', get_passnumber())
print('--------------------------------')
print('Результат вычисления функции с переданным в функцию числом', get_passnumber(17))