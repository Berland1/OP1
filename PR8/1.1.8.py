m = int(input('Введите количество строк : '))
n = int(input('Введите количество столбцов : '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
        print(b)
    a.append(b)
    print(a)
print('Исходный массив : ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

positive_sum = 0
positive_count = 0
for i in range(len(a)):
    print(a[i][i])
    positive_sum +=a[i][i]
    positive_count += 1
print('Сумма положительных чисел : ', positive_sum)
print('Количество положительных элементов : ', positive_count)