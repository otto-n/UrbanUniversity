# Список оценок студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Неупорядоченное множество имен студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Словарь в который будем записывать средний результат оценок для студентов
grades_average = {}

# Меняем тип из множества в список и упорядочиваем последовательность имён – students
students = sorted(list(students))

# Создаем записи в словаре, где ключом является имя студента (исходим из последовательности уже упорядоченного списка
# имен students). Значение каждой записи в словаре (средней оценки) мы высчитываем следующим образом:
#
# 1. Зная, что последовательность упорядоченного списка имен студентов соответствует списку значений
#    оценок студентов, обращаемся к этим значениям по индексу, который равен индексу имени студента.
# 2. Суммируем все оценки, которые есть у студента, считаем их количество и делим одно на другое.
# 3. Результат записываем, как значение (value) для каждого студента, который будет потом доступен при обращении к
#    словарю по имени студента.
#
grades_average.update({
    students[0]: sum(grades[0])/len(grades[0]),
    students[1]: sum(grades[1])/len(grades[1]),
    students[2]: sum(grades[2])/len(grades[2]),
    students[3]: sum(grades[3])/len(grades[3]),
    students[4]: sum(grades[4])/len(grades[4])
})

print(grades_average)