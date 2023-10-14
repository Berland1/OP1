n = int(input('Введите число n <= 9:' ))
for i in range(1, n + 1):
    for i1 in range(1, i + 1):
        print(i1, sep='', end='')
    print()