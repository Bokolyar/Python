# l4.dz6
from itertools import count, cycle
from random import randint


print('Выводим работу метода count')
iter_el1 = count(int(input('Введите целое число: ')))
while True:
    cur_elem = next(iter_el1)
    print(cur_elem, end=' ')
    if cur_elem == 10:
        break
print('\n', '*'*50)

print('Выводим работу метода cycle')
my_list = [randint(1, 100) for i in range(5)]
print(my_list)

iter_el2 = cycle(my_list)
elem_count = int(input('Введите целое число повторений: '))
while True:
    cur_elem = next(iter_el2)
    print(cur_elem, end=' ')
    elem_count -= 1
    if elem_count == 0:
        break
