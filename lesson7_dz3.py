class cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'cell({self.cell})'

    def __add__(self, other):
        return cell(self.cell + other.cell)

    def __sub__(self, other):
        return cell(self.cell - other.cell) if self.cell - other.cell > 0 else 'вычитание невозможно'

    def __mul__(self, other):
        return cell(self.cell * other.cell)

    def __truediv__(self, other):
        return cell(self.cell // other.cell)

    '''ВАРИАНТ 1'''
    def make_order(self, raw):
        x = ''
        n = 0
        m = 0
        while n < self.cell:
            n += 1
            m += 1
            x += '*'
            if m == raw:
                x += '\n'
                m = 0
        return x

    '''ВАРИАНТ 2'''
    def make_order2(self, raw):
        a = self.cell // raw
        b = self.cell % raw
        return ('*'*raw+'\n')*a + '*'*b


cell_1 = cell(12)
cell_2 = cell(17)
cell_3 = cell(4)

print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 / cell_3)
print('_'*40)
print(cell_2.make_order(5))
print('_'*40)
print(cell_2.make_order2(4))
