print(' ')
print('2. Вывод на одной строке')
header = ['Название', 'EmojiXpress, млн', 'Instagram, млн', 'Твиттер, млн']
# сначала напечатайте одну вертикальную черту
print('|', end='')

for name in header:
    # поставьте пробел
    print(' ', end='')

    # напечатайте очередное название из "шапки"
    print(name, end='')

    # поставьте еще один пробел и вертикальную черту
    print(' |', end='')

print(' ')
print(' ')
print('3. Методы в Python')
#Python существует функция sort()

emojixpress = [
    2.26,
    19.1,
    25.6,
    233.0,
    15.2,
    22.7,
    64.6,
    87.5,
    6.81,
    6.0,
    4.72,
    24.7,
    21.7,
    10.0,
    118.0,
    3.31,
    23.1,
    1.74,
    4.5,
    0.0333,
]

emojixpress.sort()

print(emojixpress)


emoji_names = [
    'Ухмыляюсь',
    'Сияю от радости',
    'Катаюсь от смеха',
    'Слёзы радости',
    'Подмигиваю',
    'Счастлив',
    'Глаза-сердца',
    'Целую',
    'Задумчивость',
    'Равнодушие',
    'Солнечные очки',
    'Громко плачу',
    'След от поцелуя',
    'Два сердца',
    'Сердце',
    'Червы',
    'Класс',
    'Пожимаю плечами',
    'Огонь',
    'Переработка',
]

emoji_names.sort()
for name in emoji_names:
    print(name)
print('Чтобы вывести список по порядку возрастания, был применен метод sort() ')

print(' ')
print(' ')
print('4. Булевы значения True и False. Аргументы метода sort()')

twitter = [
    87.3,
    150,
    0.0,
    2270.0,
    264.0,
    565.0,
    834.0,
    432.0,
    0.0,
    478.0,
    198.0,
    654.0,
    98.7,
    445.0,
    1080.0,
    697.0,
    227.0,
    0.0,
    150.0,
    932.0,
]

# вызовим метод sort() у переменной twitter с ключом reverse=True
twitter.sort(reverse = True)


for count in twitter:
    print(count)
print('Чтобы вывести список по порядку убывания, был применен ключ reverse ')


print(' ')
print(' ')

print('5. Сортировка по столбцу')

#ЗАДАЧА

# Отсортируйте таблицу по столбцу «Instagram, млн» по убыванию и выведите её в наглядном формате (см. прекод)
# Обратите внимание, какие эмодзи наиболее популярны на этой платформе

# SOLUTION

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

# < напишите код здесь >
data.sort(key=lambda row: row[2], reverse = True)

print('Название эмодзи  | EmojiXpress, млн |', end='')
print(' Instagram, млн | Твиттер, млн')
print('-------------------------------------', end='')
print('------------------------------')
for row in data:
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(
        row[0], row[1], row[2], row[3]))

print(' ')
print(' ')

########################################################################################################################

# 5.2 - Сортировка по столбцу

# Отсортируйте таблицу по столбцу «Твиттер, млн» по убыванию и выведите её в наглядном формате (см. прекод)
# Обратите внимание, какие эмодзи наиболее популярны на этой платформе. Какой артефакт (необычный объект) выделяется
# особо?

# SOLUTION

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

# < напишите код здесь >

data.sort(key=lambda row: row[3], reverse=True)

print('Название эмодзи  | EmojiXpress, млн |', end='')
print(' Instagram, млн | Твиттер, млн')
print('-------------------------------------', end='')
print('------------------------------')
for row in data:
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(
        row[0], row[1], row[2], row[3]))

print(' ')
print(' ')

print('6. Срезы')
# Обновите код, чтобы в каждом из трёх случаев выводилась не вся таблица, а только её первые пять строк

# SOLUTION

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

data.sort(key=lambda row: row[1], reverse=True)

# мы оставили только тот столбец, по которому сортировали
print('Название эмодзи  | Emojixpress, млн')
print('-----------------------------------')
for row in data[:5]:
    print('{: <16} | {: >16.2f}'.format(row[0], row[1]))
print()
print()

data.sort(key=lambda row: row[2], reverse=True)

# мы оставили только тот столбец, по которому сортировали
print('Название эмодзи  | Instagram, млн')
print('---------------------------------')
for row in data[:5]:
    print('{: <16} | {: >14.2f}'.format(row[0], row[2]))
print()
print()

data.sort(key=lambda row: row[3], reverse=True)

# мы оставили только тот столбец, по которому сортировали
print('Название эмодзи  | Твиттер, млн')
print('-------------------------------')
for row in data[:5]:
    print('{: <16} | {: >12.2f}'.format(row[0], row[3]))
print()
print()