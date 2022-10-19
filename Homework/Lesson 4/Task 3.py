print('Введите выставленную температуру (градусы):')
a = int(input())
print('Введите текущую температуру (градусы):')
b = int(input())
print('Введите влажность (%):')
v = int(input())
if a < b and 80 >= v:
    print('on')
else:
    print('off')
