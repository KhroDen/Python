

def test():
    number = int(input("Введите целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Вы ввели 0")


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


test()
