n = int(input())
i = 0
num = 0
while n > 0:
    i = n % 10
    n = n // 10
    if i == 9:
        num += 1
if num > 0:
    print('Есть цифра 9')
else:
    print('Нет цифры 9')