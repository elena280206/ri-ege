a = [1, 3, 5, 8, 22, 14, 98, 11, 3, -5, -49, 17, 129, -14, -879, 150]
print(len(a))
print(a[-1:])
print(a[::-1])
print('Yes' if '3' and '879' in a else 'NO')
spisok = []
for i in a:
    if i < 0:
         spisok.append(i)
print(spisok)