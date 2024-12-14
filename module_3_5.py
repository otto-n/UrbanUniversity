def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)
    # Записываем первый символ строки
    first = int(str_number[0])

    # если в строковом представлении числа больше одного символа (подразумевается 2-х значное и более число)
    if len(str_number) > 1:
        # возвращаем произведение первой цифры числа и рекурсивный результат выполнения функции
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # если число однозначное, то проверяем чтобы это был не 0 и возвращаем его, если ноль возвращаем 1
        if first == 0: return 1
        else: return first

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)