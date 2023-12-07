
year_t = int(input("Введи год, а я те кой чё скажу - "))
def is_year_leap(year):
    if year % 4 == 0:
        print('Год ', str(year), '- високосный')
        return True
    else:
        print('Год ', str(year), '- не високосный')
        return False

task = is_year_leap(year_t)
print(task)