# l3dz4

def my_func(a, b):
    # z = 1/a**b
    z = 1
    for i in range(-b):
        z *= a
    return 1/z


while True:
    x = int(input('Введите положительное целое число x: '))
    if x <= 0:
        continue
    break
while True:
    y = int(input('Введите отрицательное целое число y: '))
    if y >= 0:
        continue
    break
print(f'{x} в степени {y} = {my_func(x, y)}')
