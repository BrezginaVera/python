"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class Warehouse:
    def __init__(self, name, amount):
        self.name = name #название устройства
        self.amount = amount #количество устройства

    def __str__(self):
        return f'На складе имеется - {self.name} в количестве - {self.amount}'


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