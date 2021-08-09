class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        #print(f"Новая машина {self.name} (цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name} Машина поехала!")

    def stop(self):
        print(f"{self.name} Машина остановилась")

    def turn(self, direction):
        print(f'{self.name} Машина повернула {"налево" if direction == 0 else "Направо"}')

    def show_speed(self):
        return f"{self.name} Машина развила скорость {self.speed} км\ч"
        # print(f"{self.name} Скорость у авто {self.speed}")


class TownCar(Car):
    def show_speed(self):
        return f"{self.name} Скорость у авто {self.speed} Превышение скорости!!!" \
            if self.speed > 60 else f"Допустимая скорость {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} Скорость у авто {self.speed} Превышение скорости!!!" \
            if self.speed > 40 else f"Допустимая скорость {self.speed}"


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Полицейская", "черный", 77)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

town_car = TownCar("Chevrolet", "пурпурный", 66)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()

work_car = WorkCar("Минивен", "салатовый", 50)
work_car.go()
print(work_car.show_speed())
town_car.turn(1)
town_car.stop()
print()