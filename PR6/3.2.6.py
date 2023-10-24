n = int(input('Введите длинну массива :'))
d =[]
for i in range(n):
    d.append(float(input()))
    if i < 15:
        d[i] = d[i] * 2
    else:
        d[i] = d[i] * 1
print(d)