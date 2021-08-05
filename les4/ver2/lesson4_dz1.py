# l4.dz1
from sys import argv


name, work_hours, rate, reward = argv
print(name)
print(f'выработка в часах: {work_hours}')
print(f'ставка в час: {rate}')
print(f'премия: {reward}')

salary = int(work_hours) * int(rate) + int(reward)
print(f'зарплата = {salary}')
