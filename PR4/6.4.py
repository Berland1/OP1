n = int(input('Введите число факториала:'))
n_zn = 1
for i in range(1, n + 1, 1):
    n_zn *= i
print(n_zn)