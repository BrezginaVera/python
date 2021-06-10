class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if int(self.amount - other.amount) > 0:
            return Cell(self.amount - other.amount)
        else:
            return "Ошибка!"

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.amount / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.amount % cells_in_row)}'
        return row


cells_1 = Cell(33)
cells_2 = Cell(15)
print(cells_1)
print(cells_2)
print(cells_1 + cells_2)
print(cells_1 - cells_2)
print(cells_2 - cells_1)
print(cells_1.make_order(5))
print(cells_2.make_order(10))




