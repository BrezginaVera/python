"""Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""


class Warehouse:
    def __init__(self, name, amount, *args):
        self.name = name #название устройства
        self.amount = amount #количество устройства
        self.store = [] #передача в определенное место в компании
        self.total = {'Модель': self.name, 'Количество': self.amount}

    def __str__(self):
        return f'На складе имеется - {self.name} в количестве - {self.amount}'

    def reception(self):
        try:
            unit = input(f'Введите название: ')
            unit_amount = int(input(f'Введите количество товара: '))
            unit_total = {'Модель': unit, 'Количество': unit_amount}
            self.total.update(unit_total)
            self.store.append(self.total)
            print(f'Текущий список - {self.store}')
        except:
            return f'Ошибка'

        stop = input("Если Вы хотите остановить работу, введите - stop: ")
        if stop == 'stop':
            return (f'Итог -{self.store}')


class Hardware:
    def __init__(self, name, amount, production, use, num, time):
        self.name = name
        self.amount = amount
        self.production = production
        self.use = use
        self.num = num #количество страниц в минуту
        self.time = time #за время

    def __str__(self):
        return f'На складе имеется - {self.name} в количестве - {self.amount}, производитель - {self.production}, ' \
               f'{self.name} предназначен для {self.use}'


class Printer(Hardware):
    def numbers_in_min(self):
        return f'{self.name} печатает {self.num} страниц в минуту'


class Scanner(Hardware):
    def scan_time(self):
        return f'{self.name} сканирует за {self.time}'


class Xerox(Hardware):
    def copy(self):
        return f'{self.name} копирует {self.num} страниц в минуту'