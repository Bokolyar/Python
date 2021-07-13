class Road:
    def __init__(self, l1, w1):
        self._length = l1
        self._width = w1
        print("Дорога создана!")

    def calc(self):
        print(f"Масса асфальта для вашей дороги с длиной: {self._length}м и шириной: "
              f"{self._width}м: {self._length*self._width*25*5/1000} тонн")


a = Road(20, 5000)
a.calc()
b = Road(10, 1000)
b.calc()
