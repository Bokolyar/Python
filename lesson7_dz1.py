class Matrix:
    def __init__(self, m1):
        self.m1 = m1

    def __str__(self):
        matrix = ''
        for i in self.m1:
            z = ''
            for j in i:
                z += f'{j:^4}'
            matrix += z + '\n'
        return matrix

    def __add__(self, other):
        try:
            for i in range(len(self.m1)):
                # print(i)
                for j in range(len(self.m1[i])):
                    a = self.m1[i][j]+other.m1[i][j]
                    self.m1[i][j] = a
            return Matrix(self.m1)
        except IndexError:
            return f'Вы ввели матрицы разных размеров'


m1 = Matrix([[1, 2, 3, 44], [33, 4, 5, 6], [11, 8, 9, 104]])
m2 = Matrix([[3, 3, 2, 8], [4, 4, 1, 1], [22, 33, 1, 5]])
m3 = m1 + m2
print(m3)
