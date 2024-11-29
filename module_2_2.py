first  = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
third  = int(input('Введите третье число:'))

# если первое число равно второму, а второе третьему значит все числа равны
if first == second and second == third:
    print('3')
# если хоть одно число из трех равно какому-то числу и еще одно число равно какому-то другому числу, значит
# найдено уже не три числа равных между собой, а два (если бы три, выполнилось бы условие выше)
elif (first == second or second == third or third == first) and (first == second or second == third or third == first):
    print('2')
# если числа между собой не равны
elif not first == second and not second == third:
    print('0')
# на всякий случай, если сценарий пошел не по плану, говорим об этом
else:
    print('Что-то пошло не так')