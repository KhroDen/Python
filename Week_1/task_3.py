# Задание 3
#
# Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список. На экран выводит их сумму, максимальное и минимальное из них. Для нахождения суммы, максимума и минимума воспользуйтесь встроенными в Python функциями sum(), max() и min().




number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
number4 = int(input("Введите четвертое число: "))
number5 = int(input("Введите пятое число: "))
number6 = int(input("Введите шестое число: "))
number7 = int(input("Введите седьмое число: "))
number8 = int(input("Введите восьмое число: "))

numbersList = [number1, number2, number3, number4, number5, number6, number7, number8]

maxNumber = max(numbersList)
minNumber = min(numbersList)
sumNumbers = sum(numbersList)

print("Максимальное число списка: ", maxNumber)
print("Минимальное число списка: ", minNumber)
print("Сумма всех чисел списка: ", sumNumbers)

