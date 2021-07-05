# l4.dz1
from sys import argv


name, param1, param2, param3 = argv
print(name)
print(f'выработка в часах: {param1}')
print(f'ставка в час: {param2}')
print(f'премия: {param3}')

zp = int(param1)*int(param2) + int(param3)
print(f'зарплата = {zp}')
