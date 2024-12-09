# объявляем функцию и принимаем 1 обязательное значение и неограниченную последовательность значений
def single_root_words(root_word, *other_words):
    # объявляем пустой список, сюда будем записывать результат выполнения
    same_words = []

    # перебираем параметр с произвольным числом значений
    for string in other_words:
        # приводим строковые значения в верхний регистр, чтобы он не повлиял на сравнения
        # ищем совпадения корневых слов
        if root_word.upper() in string.upper() or string.upper() in root_word.upper():
            # при совпадении добавляем в конец списка
            same_words.append(string)

    # возвращаем список и заканчиваем выполнение функции
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)