print('Введите первое число')
a1 = int(input())
print('Введите первую букву')
b1 = input()
print('Введите второе число')
a2 = int(input())
print('Введите вторую букву')
b2 = input()
n = 0
if a1 == a2:
    n = n + 1
if b1 == b2:
    n = n + 1
if n >= 1:
    print('Yes')
else:
    print('No')