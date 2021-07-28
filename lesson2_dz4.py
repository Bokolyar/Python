# l2.dz4

text = input('Введите любую строку из нескольких слов: ').split(' ')
for i, item in enumerate(text):
    print(f'{i+1}-е слово: {item[:10]}')
