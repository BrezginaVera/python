"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
 Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной
 в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        self.weigth = 25
        self.tickness = 5
        mass = (self._length*self._width*self.weigth*self.tickness)/1000
        print(f"Масса асфальта, необходимого для покрытия все дороги: {mass} т")


road = Road(20, 5000)
road.mass()