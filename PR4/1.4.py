a = int(input('Введите числа:'))
b = int(input('Введите числа:'))
if a<=b:
    for i in range(a,b + 1):
        print(i, end=';')
else:
    print('Числа неверные')