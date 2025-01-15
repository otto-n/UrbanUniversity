def custom_write(file_name, strings):

    # Сначала опустошаем файл (чтобы номера строк из примера записывались правильно).
    clear_file = open(file_name, 'w')
    clear_file.write('')
    clear_file.close()

    # Открываем файл на запись в конец файла (append)
    file = open(file_name, 'a', encoding='utf-8')
    # Подсчитываем сколько строк нужно будет записывать в файл.
    total_rows = len(strings)
    strings_positions = dict()

    for i in range(0, total_rows):
        # Пополняем словарь, где ключ - кортеж (<номер строки, начиная с 1>, <байт начала строки>),
        # а значением - записываемая строка.
        strings_positions.update({(i+1, file.tell()): str(strings[i])})
        # Записываем в конец файла строку с переносом на новую строку.
        file.write(strings[i] + "\n")

    # Закрываем файл.
    file.close()
    # Возвращаем созданный словарь.
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)