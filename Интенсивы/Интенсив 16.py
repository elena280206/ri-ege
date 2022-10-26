a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 < a2 and b1 < b2 and b1 < a2) or (a2 < a1 and b2 < b1 and b2 < a1):
    print('Пустое множество')
elif a2 == b1 or a1 == b2:
    print('Точка')
else:
    print('Отрезок')