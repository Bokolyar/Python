# l4.dz6
from itertools import count, cycle, islice
from random import randint

my_list = [randint(1, 100) for i in range(5)]

# print([i for i in islice(count(3), 10)])
# print([i for i in islice(cycle(my_list), 15)])

print('Выводим работу метода count')
abc = count(3)
el = 0
while el < 10:
    el = next(abc)
    print(el)
print('*'*50)
print('Выводим работу метода cycle')
print(my_list)
cde = cycle(my_list)
i = 0
while i < len(my_list)*2:
    el = next(cde)
    print(el)
    i += 1
