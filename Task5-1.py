"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

my_list = []
while True:
    line = input("Введите строку: ")
    if line == " ":
        exit()
    else:
        new_line = line + "\n"
        my_list.append(new_line)

    my_file = open("for Task5-1.txt", "w")
    my_file.writelines(my_list)


my_file.close()
