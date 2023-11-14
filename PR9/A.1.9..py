import math
x = int(input('Введите значение "x" : '))
n = int(input('Введите значение "n" : '))

def calculate(x, n):
    sqrt = x ** n
    factorial = math.factorial(n)
    result = sqrt / factorial
    return  result
result_last = calculate(x, n)
print('Результат : ', result_last)