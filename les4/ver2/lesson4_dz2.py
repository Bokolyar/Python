# l4.dz2
from random import randint
# p_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
p_list = [randint(0, 100) for el in range(14)]

new_list = [p_list[i] for i in range(1, len(p_list)) if p_list[i] > p_list[i-1]]
print(p_list)
print(new_list)
