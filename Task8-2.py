"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class DivisionNull(Exception):
    def __init__(self, dividend, division):
        self.dividend = dividend
        self.division = division


    def devide_null(self, dividend, division):
        try:
            return (dividend/division)
        except:
            return ("Деление на 0!")


div = DivisionNull(7,5)
print(div.devide_null(8,18))
print(div.devide_null(0,856))
print(div.devide_null(69,0))
