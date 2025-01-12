import math

class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = tuple()
        self.__color = tuple()
        self.filled = bool()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, rgb):
        # Перебираем кортеж rgb и проверяем чтобы в нем были целые числовые значения в диапазоне от 0 до 255 (включительно)
        if not all(isinstance(c, int) and 0 <= c <= 255 for c in rgb):
            # Если что-то не совпало - проверка не прошла
            return False
        return True

    def set_color(self, *rgb):
        if self.__is_valid_color(rgb):
            self.__color = rgb

    def __is_valid_sides(self, *new_sides):
        # Сравниваем количество сторон для фигуры, а также перебираем кортеж со сторонами и проверяем чтобы в нем были
        # положительные, целые числовые значения
        if not all(len(self.__sides)==len(new_sides) and isinstance(new_side, int) and new_side >= 0 for new_side in new_sides):
            return False
        return True

    def get_sides(self):
        return self.__sides

    # Магический метод (перегрузка) для вычисления суммы сторон
    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        # Если количество сторон совпадает, перезаписываем на новые значения
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides

# Круг
class Circle(Figure):
    sides_count = 1
    
    def __init__(self, new_color, *new_sides):
        super().__init__() # наследуем все что есть у родителя при создании класса
        self.set_color(*new_color) # определяем цвет фигуры
        self.set_sides(*new_sides) # определяем размер стороны (окружности)

        # Если передаваемое количество сторон не совпадает с требуемым
        if len(new_sides) != self.sides_count:
            # Определяем, что каждая сторона равна значению 1 (в данном случае это одна сторона - окружность)
            self.set_sides((1,)*self.sides_count)

        # Т.к. у нас это круг, определяем радиус (длину 1й стороны)
        self.__radius = self.get_sides()[0]

    # Метода для вычисления площади окружности через радиус (Значение "Пи" в квадрате), для удобочитаемости
    # оставляем 2 символа после плавающей точки.
    def get_square(self):
        return round(math.pi * self.__radius ** 2, 2)

# Треугольник
class Triangle(Figure):
    sides_count = 3

    def __init__(self, new_color, *new_sides):
        super().__init__()
        self.set_color(*new_color)
        self.set_sides(*new_sides)

        if len(new_sides) != self.sides_count:
            self.set_sides((1,)*self.sides_count)


    def get_square(self):
        # Берем все стороны треугольника
        sides = self.get_sides()
        # Вычисляем полупериметр
        semi_perimeter = sum(sides) / 2
        #  Возвращаем площадь треугольника по "формуле Герона", ограничиваемся 2 цифрами после плавающей точки
        return round(math.sqrt(semi_perimeter * (semi_perimeter - sides[0]) * (semi_perimeter - sides[1]) * (
                semi_perimeter - sides[2])), 2)

# Куб
class Cube(Figure):
    sides_count = 12

    def __init__(self, new_color, *new_sides):
        super().__init__()
        self.set_color(*new_color)

        if len(new_sides) != self.sides_count:
            self.set_sides((1,)*self.sides_count)

        # Если при создании куба было передано только одно значение для сторон, то размножаем их до 12
        if len(new_sides) == 1:
            cube_sides = (new_sides[0],) * 12
            self.set_sides(*cube_sides)

    # Вычисляем объем куба (берем для этого значение одной стороны)
    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10, 11, 12) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())