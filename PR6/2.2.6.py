import random
a = [random.random() for g in range(-10,10)]
a2 = []
a3 = []
for i in a:
    if (i < 0):
        a3.append(i)
    elif (i == 0):
        a3.append(i)
    else:
        a2.append(i)
print(a)
print(a2)
print(a3)