def month_to_season(month_n):
    month_n = int(month_n)
    if month_n <= 0 or month_n > 12:
        print("У тебя всё в порядке? Нужен номер месяца")
    elif 1 < month_n <= 2 or month_n == 12:
        print("Зима")
    elif 3 <= month_n <= 5:
        print("Весна")
    elif 6 <= month_n <= 8:
        print('Лето')
    else:
        print("Осень")

month_to_season(input("Введи номер месяца - "))