   
# def treugolnick(a, b, c):
#   print (f'Результат: Треугольник со сторонами', a, b, c, end=' ')
#   if a > b + c or b > a + c or c > a + b:
#     print (f'не возможен')
#   elif c**2 == a**2 + b**2 or a**2 == c**2 + b**2 or b**2 == a**2 + c**2:
#     print (f'прямоугольный')
#   elif c**2 > a**2 + b**2 or a**2 > c**2 + b**2 or b**2 > a**2 + c**2:
#     print (f'тупоугольный')
#   elif c**2 < a**2 + b**2 or b**2 < a**2 + c**2 or a**2 < c**2 + b**2:
#     print (f'остроугольный')
#   else:
#     print(f'???')
# print(f'Введите построчно 3и стороны треугольника')
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# treugolnick(a, b, c)

def func(a, b, oper):
    if oper == "sum":
        result = a + b
    elif oper == "sub":
        result = a - b
    elif oper == "div":
        if b == 0:
            return 'Ало! На 0 нельзя делить!'
        else:
            result = a / b
    elif oper == "mult":
        result = a * b
    else:
        return "Действия: sum для складывания, sub для вычитания, div для деления и mult для умножения, ОК?"
    return result

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
oper = input("Введите математическое действие (sum для складывания, sub для вычитания, div для деления и mult для умножения): ")
result = func(a, b, oper)
print(f"Результат: {result}")
    