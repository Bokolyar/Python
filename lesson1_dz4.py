# dz4

print(f'Программа для поиска самой большой цифры в числе')
data = int(input('Введите целое положительное число: '))
digit = data
result = digit % 10
while True:
    if digit // 10 > 0:
        a = digit // 10 % 10
        if result < a:
            result = a
        digit = digit // 10
        continue
    break
print(f'Максимальная цифра в числе {data}: {result}')
