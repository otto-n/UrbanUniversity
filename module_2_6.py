import random

def get_passnumber(number = random.randint(3,20)):
    print('Пароль для номера:', number)
    two_stone = []

    for i in range(1, number + 1):
        for j in range(2, number + 1):
            if (number % (i + j) == 0) and not [j, i] in two_stone:
                two_stone.append([i, j])

    return two_stone

print(get_passnumber())