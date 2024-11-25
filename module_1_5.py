immutable_var = ('one', 2, True)
print(immutable_var)

# закомментированный код ниже не выполнится, т.к. изменить значение
# элемента кортежа нельзя, это неизменяемый объект
# immutable_var[1] = str(immutable_var[1])
# print(immutable_var)

mutable_list = ['one', 2, True, 'three']
print(mutable_list)

mutable_list[3] = 3
print(mutable_list)