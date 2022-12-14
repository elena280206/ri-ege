n = input()
n1 = len(n)
m = input()
i1 = 0
i2 = 0
h = ''
for i in range(n1):
    if n[i] == m:
        i1 += i
        break
h = len(n[i:])
h1 = len(n[:i + 1])
for j in range(h):
    if n[j] == m:
        i2 = j
if i1 == 0 and i2 == 0:
    print('Символа ', m, ' в строке ', n, ' нет')
else:
    print('Номер первого вхождения символа ', m, ' в строку ', n, ' - ', i1)
    print('Номер последнего вхождения символа ', m, ' в строку ', n, ' - ', i2)