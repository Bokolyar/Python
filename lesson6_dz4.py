class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} "{self.name}" start moving with speed {self.speed} km/h!')

    def stop(self):
        print(f'{self.color} "{self.name}" stop moving')

    def turn(self, direction):
        print(f'{self.color} "{self.name}" turn {direction}')

    def show_speed(self):
        print(f'{self.color} "{self.name}" is moving with speed {self.speed} km/h!')


class TownCar(Car):
    def show_speed(self):
        print("Превышение скорости") if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        print("Превышение скорости") if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


A = Car(100, 'red', 'Lada', 0)
A.go()
A.stop()
A.turn('left')
A.turn('right')
A.show_speed()
B = TownCar(70, 'blue', 'BMW', 0)
B.go()
B.show_speed()
C = WorkCar(50, 'grey', 'Трактор', 0)
C.go()
C.show_speed()
D = WorkCar(30, 'grey', 'Снегоуборочная машина', 0)
D.go()
D.show_speed()
