a = print('Введите выставленную температуру (градусы):'), input()
b = print('Введите текущую температуру (градусы):'), input()
n = print('Введите влажность (%):'), input()
if b < a and 80 < n:
    print('on')
else:
    print('off')