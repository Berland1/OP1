from  random import *
b = [randint(1,100) for g in range(10)]
sum_elements = sum(b)
sr = sum_elements/len(b)
for i in range(len(b)):
    if b[i] == 0:
        b[i] = sr
print(b)