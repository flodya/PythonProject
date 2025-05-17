
class car:
    def __init__(self, speed):
        self.speed = speed

    def speed(self):
        print(f" швидкість {self.speed} км/год.")


class cars(car):
    def speed(self):
        print(f" швидкість {self.speed} км/год.")


class pilot(car):
    def speed(self):
        print(f"видкість літака  {self.швидкість} км/год.")


class hs(car):
    def speed(self):
        print(f"корабль пливе  {self.швидкість} км/год.")

# Тестування
car = car(120)
cars = cars(800)
hs = hs(40)

car.переміщення()
cars.переміщення()
hs.переміщення()
