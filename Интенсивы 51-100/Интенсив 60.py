a = input()
b = input()
i = 0
if a in b and len(a) != len(b):
    print('Строка', a, 'является вложенной в строку', b)
if b in a and len(a) != len(b):
    print('Строка', b, 'является вложенной в строку', a)
if a == b:
    print('Строки совпадают полностью')
while i < len(a) and i < len(b):
    if a[i] != b[i]:
        print('Строки начинают различаться с символа', i)
        exit()
    i += 1