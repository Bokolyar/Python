# dz2

print("Эта программа переводит секунды в часы, минуты, секунды в формате чч:мм:сс")
while True:
    Seconds = int(input("Введите любое количество секунд: "))
    if Seconds <= 0:
        print("Ввод неверный. Число секунд должно быть положительным")
        continue
    break
Hours = Seconds // 3600
Minutes = Seconds % 3600 // 60
Seconds = Seconds % 60
# print('{:02}:{:02}:{:02}'.format(Hours, Minutes, Seconds))
print(f'{Hours:02}:{Minutes:02}:{Seconds:02}')

