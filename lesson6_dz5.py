class Stationary:
    def __init__(self, title):
        self.title = title
        print("Создан канцелярский объект", self.title)

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def __init__(self):
        self.title = "Pen"

    def draw(self):
        print('Запуск отрисовки with Pen')


class Pencil(Stationary):
    def __init__(self):
        # определяем атрибут самостоятельно
        self.title = 'Pencil'
        print("Создан канцелярский объект", self.title)

    def draw(self):
        print('Запуск отрисовки with Pencil')


class Handle(Stationary):
    def __init__(self):
        # используем родительский метод
        super().__init__("Handle")

    def draw(self):
        print('Запуск отрисовки with Handle')


A = Stationary('Карандаш')
print(A.title)
A.draw()
print('*'*50)
B = Pen()
print(B.title)
B.draw()
print('*'*50)
C = Handle()
C.draw()
print('*'*50)
D = Pencil()
print(D.title)
D.draw()


