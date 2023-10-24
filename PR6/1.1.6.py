n = int(input('Введите массив с клавиатуры: '))
a = []
for i in range(n):
    a.append(float(input()))
print(a)
max_elements = max(a)
obr = a[::-1]
print(max_elements)
print(obr)