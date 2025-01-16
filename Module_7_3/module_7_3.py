class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def _read_file(self, file_name):
        """Читает файл и возвращает список слов в нижнем регистре без знаков препинания."""
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            # Убираем знаки ненужные символы
            chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
            for char in chars:
                text = text.replace(char, '')
            return text.split()

    def get_all_words(self):
        """Возвращает словарь, где ключ — имя файла, значение — список всех слов."""
        return {file_name: self._read_file(file_name) for file_name in self.file_names}

    def find(self, word):
        """Ищет первое вхождение слова в каждом файле и возвращает словарь с позициями."""
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Индексация с 1
        return result

    def count(self, word):
        """Считает количество вхождений слова в каждом файле."""
        word = word.lower()
        return {file_name: words.count(word) for file_name, words in self.get_all_words().items() if word in words}


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))     # Позиция первого вхождения слова
print(finder.count('teXT'))    # Количество вхождений слова