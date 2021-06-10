""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл."""

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
my_file = open("for Task5-4.txt", "r")
for i in my_file:
    i = i.split(' ', 1)
    new_file.append(rus[i[0]] + '  ' + i[1])
print(new_file)
my_file.close()
my_file_new = open("for Task5-4_new.txt", "w")
my_file_new.writelines(new_file)

my_file_new.close()




