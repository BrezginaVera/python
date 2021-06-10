""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        self.direction = direction
        return f"Машина {self.name} повернула {direction}"

    def show_speed(self):
        return f"Текущая скорость автомобиля: {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} - {self.speed}")
        if self.speed > 60:
            return f" {self.speed} - Превышение скорости!"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} - {self.speed}")
        if self.speed > 40:
            return f" {self.speed} - Превышение скорости!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lexus = TownCar(100, 'White', 'Lexus', False)
volvo = SportCar(150, 'Brown', 'Volvo', False)
kia = WorkCar(60, 'Red', 'Kia', True)
mercedes = PoliceCar(98, 'Blue',  'Mercedes', True)
print(f'{lexus.go()} со скоростью {lexus.show_speed()}')
print(f'{kia.name} - {kia.color}')
print(f'{volvo.name} полицеская машина? {volvo.is_police}')
print(f' {mercedes.name} полицейская машина? {mercedes.is_police}')
print(volvo.show_speed())
print(kia.show_speed())
print(mercedes.show_speed())