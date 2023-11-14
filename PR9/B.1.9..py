print('Чтобы закончить программу, введите последним значением число "0" ')
def maximum():
    max = float('-inf')
    while True:
        num = int(input('Введите число с клавиатуры : '))
        if num == 0:
            break
        else:
            if num > max:
                max = num
    return  max
result = maximum()
print('Максимальное число из вашей последовательности : ', result)