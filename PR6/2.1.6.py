n = int(input('Введите массив с клавиатуры :'))
a = []
for i in range(n):
    a.append(float(input()))
print(a)
min_elements = min(a)
ind = min_elements.index()
print(min_elements)
print(ind)