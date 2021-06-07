"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

import numpy
my_file = open("for Task5-3.txt", "r")
workers = {}
mean_salary = 0
for line in my_file:
    key, value = line.split()
    workers[key] = value
    salary = int(value)
    if salary < 20000:
        print(f"{key}: зарплата меньше 20000")
    mean_salary+=salary
print(f"Средняя величина дохода составила: {numpy.mean(mean_salary)}")

my_file.close()

