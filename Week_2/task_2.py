# Задание 2
#
#
# В программировании можно из одной функции вызывать другую. Для иллюстрации этой возможности напишите программу по следующему описанию.
#
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число. Если оно положительное, то вызывается функция positive(), тело которой содержит команду вывода на экран слова "Положительное". Если число отрицательное, то вызывается функция negative(), ее тело содержит выражение вывода на экран слова "Отрицательное".
#
# Понятно, что вызов test() должен следовать после определения функций. Однако имеет ли значение порядок определения самих функций? То есть должны ли определения positive() и negative() предшествовать test() или могут следовать после него? Проверьте вашу гипотезу, поменяв объявления функций местами.
# Попробуйте объяснить результат добавив коментарии к коду.




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
