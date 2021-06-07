"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

my_file = open("for Task5-2.txt", "r")
lines = my_file.readlines()
num_lines = 0
for line in lines:
    num_lines+=1
print(f"Количество строк: {num_lines}.")
for index, value in enumerate(lines):
    num_words = len(value.split())
    print(f"Количество слов в строке: {num_words}.")

my_file.close()
