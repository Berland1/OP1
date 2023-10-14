s = str(input('Введите строку с "." '))
s2 = s.replace('.', '')
a = len(s) - len(s2)
print(s2, a)