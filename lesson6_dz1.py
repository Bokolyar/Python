from time import sleep
from turtle import speed, hideturtle,circle,up, sety, down, begin_fill, end_fill, fillcolor


class TrafficLight:
    def __init__(self, c):
        self.__color = c
        self.__n = 1    # счетчик
        print("color:", self.__color)
        speed(0)
        hideturtle()
        circle(50)
        up()
        sety(100)
        down()
        circle(50)
        up()
        sety(-100)
        down()
        circle(50)

    def running(self, color_new):
        if (self.__n + 1) % 4 == 1 and color_new == "red":
            self.__n += 1
            self.__color = color_new
            print("color:", self.__color)
            fillcolor("#ffffff")
            begin_fill()
            circle(50)
            end_fill()
            up()
            sety(100)
            down()
            fillcolor(self.__color)
            begin_fill()
            circle(50)
            end_fill()
        elif (self.__n + 1) % 2 == 0 and color_new == "yellow":
            self.__n += 1
            self.__color = color_new
            print("color:", self.__color)
            fillcolor("#ffffff")
            begin_fill()
            circle(50)
            end_fill()
            up()
            sety(0)
            down()
            fillcolor(self.__color)
            begin_fill()
            circle(50)
            end_fill()
        elif (self.__n + 1) % 4 == 3 and color_new == "green":
            self.__n += 1
            self.__color = color_new
            print("color:", self.__color)
            fillcolor("#ffffff")
            begin_fill()
            circle(50)
            end_fill()
            up()
            sety(-100)
            down()
            fillcolor(self.__color)
            begin_fill()
            circle(50)
            end_fill()
        else:
            print(f"Текущий цвет светофора: {self.__color}, слеующий цвет не может быть {color_new}")


a = TrafficLight("red")
sleep(2)
for _ in range(3):
    a.running("yellow")
    sleep(2)
    a.running("green")
    sleep(3)
    a.running("yellow")
    sleep(2)
    a.running("red")
    sleep(7)

