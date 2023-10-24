n = int(input('Введите длинну массива :'))
d =[]
sum_odd_index = 0
for i in range(n):
    d.append(float(input()))
    if i%2 != 0:
        sum_odd_index += d[i]
print(sum_odd_index)