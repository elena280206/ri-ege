n = int(input())
numbCh = 0
numbN = 0
while n > 0:
    m = n % 10
    if m % 2 == 0:
        numbCh += 1
    else:
        numbN += 1
    n = n // 10
if numbCh > numbN:
    print('Четных', numbCh)
elif numbN > numbCh:
    print('Нечетных', numbN)
else:
    print('Числа равны')