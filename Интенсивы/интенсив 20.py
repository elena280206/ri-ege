print('Введите номер клетки')
x1 = int(input())
print('Введите букву клетки')
y1 = int(input())
print('Введите номер клетки')
x2 = int(input())
print('Введите букву клетки')
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('Yes')
else:
    print('No')