input_str = input('Введите три целых числа:')
a, b, c = input_str.split()
a = int(a)
b = int(b)
c = int(c)
sum = a + b + c
cr_ar = sum // 3
print(cr_ar)