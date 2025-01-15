from os.path import split

class Product:
    def __init__(self, name, weight, category):
        self.name = name # str
        self.weight = weight # float
        self.category = category # str

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        full_data_file = self.get_products()
        list_rows = full_data_file.split("\n") # Разделяем весь текст построчно.

        # Перебираем экземпляры классов "Продукты".
        for p in products:
            # Устанавливаем флаг для продукта, который пока не найден в базе.
            exists_product = False
            for r in list_rows: # Построчно перебираем файл (точнее список строк, которые прочитаны из файла).
                if r != '' and p.name.lower() in r.lower(): # Если наименование товара нашлось в строке.
                    print(f"Продукт {p.name} уже есть в магазине") # Выводим сообщение, что продукт уже есть.
                    exists_product = True # И устанавливаем флаг, который означает, что продукт найден был в базе.
                    break # Прекращаем выполнение внутреннего цикла.
            if not exists_product: # Если флаг не изменился, значит продукт не найден
                # Перебрали все строки в файле, продукта не нашлось, значит записываем его в файл
                file = open(self.__file_name, 'a')
                file.write(f"{p.name}, {p.weight}, {p.category}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())