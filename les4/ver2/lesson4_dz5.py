# l4.dz5
from functools import reduce


def my_f(prev_el1, el1):
    return prev_el1 * el1


p_list = [el for el in range(100, 1001) if el % 2 == 0]
multiplication = reduce(my_f, p_list)
print(multiplication)
