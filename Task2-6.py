my_list=[]
my_dict={}
n = 1
while n > 0:
    n = int(input("Введите номер: "))
    n = int(n)
    if n!=0:
        val_1 = str(input("Название: "))
        val_2 = int(input("Цена: "))
        val_3 = int(input("Количество: "))
        val_4 = int(input("Ед: "))
        key_1 = "Название"
        key_2 = "Цена"
        key_3 = "Количество"
        key_4 = "Ед"
        my_dict[key_1] = val_1
        my_dict[key_2] = val_2
        my_dict[key_3] = val_3
        my_dict[key_4] = val_4
    else:
        break
    my_list.append(tuple([n, my_dict]))
print(my_list)
analitics = {}
list_val_1 = []
list_val_2 = []
list_val_3 = []
list_val_4 = []
for el in my_list:
    if val_1 in my_dict.values():
        list_val_1.append(val_1)
    if val_2 in my_dict.values():
        list_val_2.append(val_2)
    if val_3 in my_dict.values():
        list_val_3.append(val_3)
    if val_4 in my_dict.values():
        list_val_4.append(val_4)
analitics['Название'] = list_val_1
analitics['Цена'] = list_val_2
analitics['Количество'] = list_val_3
analitics['Ед'] = list_val_4
print(analitics)


