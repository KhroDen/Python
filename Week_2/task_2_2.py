def test():
    number = int(input("Введите целое число: "))
    if number > 0:
        def positive():
            print("Положительное")
        return positive()
    elif number < 0:
        def negative():
            print("Отрицательное")
        return negative()
    else:
        print("Вы ввели 0")


test()
