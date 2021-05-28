string = str(input("String: "))
my_list = string.split()
for id, val in enumerate(my_list, 1):
    print(id, val[:10])