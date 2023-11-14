a = int(input('Введите значение числа "a" : '))
b = int(input('Введите значение числа "b" : '))
def calculate(a, b):
    if a < b:
        return a
    else:
        return calculate(a - b, b)
result = calculate(a, b)
print('Остаток от деления : ', result)