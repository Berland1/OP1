n = int(input('Введите число:'))
sum = 0
n_zn = 1
for i in range(1, n + 1, 1):
    n_zn *= i
    sum += n_zn
print(sum)