"""Напишите программу, в которую вводится трехзначное числои выводятся на
экран его цифры. Например, при вводе числа 123 программа должна вывести:
1, 2, 3
"""

a = 0

while not (99 < a < 1000):
    try: a = abs(int(input("Введите трёхзначное число: ")))
    except ValueError:
        print("Вы ввели не число! Попробуйте ещё раз")
print(a//100, a%100//10, a%10, sep=', ')
