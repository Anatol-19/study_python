def square(side):
    side = int(side)
    perim = side ** 2
    return perim
print('Расчитаем перимитр квадрата')
a = input('Введите длину сороны - ')
perim = square(a)
print('Перимитр равен = ' + str(perim))