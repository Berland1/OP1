m = int(input('Введите количество строк : '))
n = int(input('Введите количество столбцов : '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [', i,',', j,'] элемент')
        b.append(int(input()))
        print(b)
    a.append(b)
    print(a)
print('Исходный массив : ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end= ' ')
    print()

for i in range(n):
    max_element = max(a[i])
    min_element = min(a[i])
    max_index = a[i].index(max_element)
    min_index = a[i].index(min_element)
    a[i][0], a[i][max_index] = a[i][max_index], a[i][0]
    a[i][-1], a[i][min_index] = a[i][min_index], a[i][-1]
print("\nРезультат:")
for row in a:
    print(row)