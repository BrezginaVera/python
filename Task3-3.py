"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(var_1, var_2, var_3):
    var_min= min(var_1, var_2, var_3)
    var_sum = sum([var_1, var_2, var_3]) - var_min
    return var_sum


print(my_func(20, 80, 30))
