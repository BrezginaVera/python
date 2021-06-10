class Clothes:
    def __init__(self, volume, height):
        self.volume = volume
        self.height = height

    def textile_coat(self):
        return self.volume/6.5 + 0.5

    def textile_costume(self):
        return 2 * self.height + 0.3

    @property
    def total_textil(self):
        return f"Общий расход ткани составляет: {(self.volume/6.5 + 0.5) + (2 * self.height + 0.3)}"


class Coat(Clothes):
    def __init__(self, volume, height):
        super().__init__(volume, height)

    def __str__(self):
        return f"Расход ткани составляет: {(self.volume/6.5 + 0.5)}"


class Costume(Clothes):
    def __init__(self, volume, height):
        super().__init__(volume, height)

    def __str__(self):
        return f"Расход ткани составляет: {(2 * self.height + 0.3)}"


coat = Coat(5, 7)
costume = Costume(7, 8)
print(coat)
print(costume)
print(coat.textile_coat())
print(costume.textile_costume())
print(coat.total_textil)

