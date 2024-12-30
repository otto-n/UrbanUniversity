class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor):

        if int(new_floor) > self.number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(1, int(new_floor)+1): # чтобы новый этаж был включен в поэтажное перечисление, увеличиваем индекс +1
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))