# l2.dz3

while True:
    month = int(input('Введите номер месяца от 1 до 12: '))
    if 1 <= month <= 12:
        break
# решение через list
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print(f'{month}-й месяц - это время года: зима')
elif month in spring:
    print(f'{month}-й месяц - это время года: весна')
elif month in summer:
    print(f'{month}-й месяц - это время года: лето')
else:
    print(f'{month}-й месяц - это время года: осень')

# решение через dict (использовал внутри словаря кортежи, вместо списков)
year = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for i in year:
    print(f'{month}-й месяц - это время года: {i}') if month in year.get(i) else None
