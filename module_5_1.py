class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):

        if int(new_floor) > self.number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(1, int(new_floor)+1): # чтобы новый этаж был включен в поэтажное перечисление, увеличиваем индекс +1
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)