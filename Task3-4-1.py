"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""

def my_func():
    x = float(input("Введите действительное положительное число: "))
    y = int(input("Введите отрицательное число: "))
    reverse_x = 1/x
    module_y = abs(y)
    if module_y!=0:
        for i in range(2, module_y+1):
            result=reverse_x*1/x
            reverse_x=result
    else:
        reverse_x=reverse_x
    return(reverse_x)


print(my_func())