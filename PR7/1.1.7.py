import math
figure = (input('Введите название фигуры : '))
s = 0
if figure == 'треугольник' or figure == 'Треугольник':
    a = float(input('Введите длинну стороны "a" : '))
    b = float(input('Введите длинну стороны "b" : '))
    c = float(input('Введите длинну стороны "c" : '))
    p = (a + b + c )/2
    s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
elif figure == 'квадрат' or figure == 'Квадрат':
    a = float(input('Введите сторону квадрата :'))
    s = a**2
elif figure == 'круг' or figure == 'Круг':
    r = float(input('Введите радиус круга :'))
    s = math.pi * (r**2)
elif figure == 'прямоугольник' or figure == 'Прямоугольник':
    a = float(input('Введите сторону "a" : '))
    b = float(input('Введите сторону "b" : '))
    s = a * b
print(s)