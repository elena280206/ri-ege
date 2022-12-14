r = 'красный'
b = 'синий'
y = 'желтый'
n = input()
m = input()
if n == r and m == b or n == b and m == r:
    print('Фиолетовый')
elif n == r and m == y or n == y and m == r:
    print('Оранжевый')
elif n == b and m == y or n == y and m == b:
    print ('Зеленый')
elif n and m == r:
    print('Красный')
elif n and m == b:
    print('Синий')
elif n and m == y:
    print('Желтый')
else:
    print('Ошибка')