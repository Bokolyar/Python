# l2.dz4

text = input('Введите любую строку из нескольких слов: ')
spis = text.split(' ')
p_lastsymbol = len(spis)
p_text = 'слова' if (p_lastsymbol % 10 == 1 and p_lastsymbol % 100 != 11) else 'слов'
print(f'Ваша строка состоит из {len(spis)} {p_text}')
for i, item in enumerate(spis):
    print(f'{i+1}-е слово: {item[:10]}')
