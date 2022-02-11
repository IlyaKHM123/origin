# Дом задание номер 3

num = int(input('Введите процент '))

percent = num
if percent == 0 or 5 <= percent <= 20:
    print(percent, 'Процентов')
if percent == 1:
    print(percent, 'Процент')
elif 2 <= percent < 5:
    print(percent, 'Процента')
if percent >= 21:
    print('Неверное значение', num, 'Ведите от 0 до 20')
