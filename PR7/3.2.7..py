string = input('Введите то, что хотите отсортировать по алфавиту : ').lower().split()
string2 = ''
for i in range(len(string)):
  string[i] = sorted(string[i])
  string2 += ','.join(string[i]) + '.'
string = string2
print('Отсортировано : ', string)