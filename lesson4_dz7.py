from itertools import count


def fact(n):
    yield 1
    a = 1
    for i in range(1, n+1):
        a *= i
        yield a


param_a = count(0)
x = int(input('n: '))
for el in fact(x):
    print(f'{next(param_a)}! = {el}')
