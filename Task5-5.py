"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import numpy
my_file = open("for Task5-5.txt", "w")
numbers = [int(i) for i in input("Введите последовательность чисел: ").split()]
str_numbers = str(numbers)
my_file.writelines(str_numbers)
print(f"Сумма чисел в файле составляет: {sum(numbers)}")

my_file.close()

