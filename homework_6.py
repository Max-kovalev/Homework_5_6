'''
Овен (21.03 – 20.04)
Телець (21.04 – 21.05)
Близнята (22.05 – 21.06)
Рак (22.06 – 22.07)
Лев (23.07 – 21.08)
Діва (22.08 – 23.09)
Терези (24.09 – 23.10)
Скорпіон (24.10 – 22.11)
Стрілець (23.11 – 21.12)
Козеріг (22.12 – 20.01)
Водолій (21.01 – 18.02)
Риби (19.02 – 20.03)
'''
month = int(input('Введіть місяць народження: '))
while month < 1 or month > 12:
    print('Помилка')
    month = int(input('Введіть місяць народження: '))
date = int(input('Введіть свій день народження: '))
while date < 1 or date > 31:
    print('Помилка')
    date = int(input('Введіть свій день народження: '))
while ((month == 4 or month == 6 or month == 9 or month == 11) and date > 30) or (month == 2 and date > 28):
    print('Помилка')
    date = int(input('Введіть свій день народження: '))
if 21 <= date <= 31 and month == 3 or month == 4 and 1 <= date <= 20:
    print("Ваш знак зодіаку: Овен")
    print("")
elif 21 <= date <= 31 and month == 4 or month == 5 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Телець")
    print("")
elif 22 <= date <= 31 and month == 5 or month == 6 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Близнята")
    print("")
elif 22 <= date <= 31 and month == 6 or month == 7 and 1 <= date <= 22:
    print("Ваш знак зодіаку: Рак")
    print("")
elif 23 <= date <= 31 and month == 7 or month == 8 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Лев")
    print("")
elif 22 <= date <= 31 and month == 8 or month == 9 and 1 <= date <= 23:
    print("Ваш знак зодіаку: Діва")
    print("")
elif 24 <= date <= 31 and month == 9 or month == 10 and 1 <= date <= 23:
    print("Ваш знак зодіаку: Терези")
    print("")
elif 24 <= date <= 31 and month == 10 or month == 11 and 1 <= date <= 22:
    print("Ваш знак зодіаку: Скорпіон")
    print("")
elif 23 <= date <= 31 and month == 11 or month == 12 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Стрілець")
    print("")
elif 22 <= date <= 31 and month == 12 or month == 1 and 1 <= date <= 20:
    print("Ваш знак зодіаку: Козеріг")
    print("")
elif 21 <= date <= 31 and month == 1 or month == 2 and 1 <= date <= 18:
    print("Ваш знак зодіаку: Водолій")
    print("")
elif 19 <= date <= 31 and month == 2 or month == 3 and 3 <= date <= 20:
    print("Ваш знак зодіаку: Риби")
    print("")

print(f'month={month}, date={date}')
