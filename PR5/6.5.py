s = str(input('Введите строку: '))
s2 = s.replace('a', '')
l = len(s) - len(s2)
print(s2, l)