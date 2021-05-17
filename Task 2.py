time = int(input("Введите время в секундах: "))
hours = time // 3600
min = (time - (hours * 3600)) // 60
sek = time - (hours * 3600) - (min * 60)
print('%d:%d:%d' % (hours, min, sek))

