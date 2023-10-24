n = int(input('Введите длинну массива :'))
d =[]
for i in range(n):
    d.append(float(input()))
    if d[i] < 15:
        d[i] = d[i] * 2
print(d)