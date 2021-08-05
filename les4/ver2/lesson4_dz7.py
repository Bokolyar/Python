# l4.dz7
def fact(n):
    yield 1
    fact_n = 1
    for i in range(1, n+1):
        fact_n *= i
        yield fact_n


x = int(input('n: '))
for index, el in enumerate(fact(x)):
    print(f'{index}! = {el}')
