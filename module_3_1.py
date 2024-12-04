calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()

    tuple_ = (len(string), string.upper(), string.lower())

    return tuple_

def is_contains(string, list_to_search):
    count_calls()

    # Для удобства использовал выражение-генератор, как он работает, разобрался из статьи на Хабре
    # для подтверждения понимания (а не просто скопировал и вставил):
    # list_to_search – вводное значение для цикла;
    # item (который слева от in) – один из элементов списка list_to_search;
    # item (который слева от for) – финальное выражение (результат итерации), к которому применяем метод перевода
    # строки в нижний регистр;
    if string.lower() in (item.lower() for item in list_to_search):
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)