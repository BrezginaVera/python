"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.complex_num = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма complex_num_1 и complex_num_2: ')
        return f'complex_num = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение complex_num_1 и complex_num_2: ')
        return f'complex_num = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'complex_num = {self.a} + {self.b} * i'


complex_1 = ComplexNumber(78, 369)
complex_2 = ComplexNumber(-123, 4)
print(complex_1)
print(complex_1 + complex_2)
print(complex_1 * complex_2)