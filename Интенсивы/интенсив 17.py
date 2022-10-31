r = 'красный'
b = 'синий'
y = 'желтый'
n = input()
m = input()
if n or m == r and n or m == b:
    print('Фиолетовый')
elif n or m == r and n or m == y:
    print('Оранжевый')
elif n or m == b and n or m == y:
    print ('Зеленый')
elif n and m == r:
    print('Красный')
elif n and m == b:
    print('Синий')
elif n and m == y:
    print('Желтый')
else:
    print('Ошибка')