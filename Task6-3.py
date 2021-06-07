"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
       super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return {'name': self.name, 'surname': self.surname}

    def get_total_income(self):
        return {'wage': self.wage, 'bonus': self.bonus}


worker_1 = Position('Igor', 'Ivanov', 'intern', 50, 70)
worker_2 = Position('Sergey', 'Petrov', 'manager', 100, 50)
worker_3 = Position('Maria', 'Isaeva', 'designer', 200, 80)
print(worker_1.get_full_name(), worker_1.get_total_income())
print(worker_2.get_full_name(), worker_2.get_total_income())
print(worker_3.get_full_name(), worker_3.get_total_income())
