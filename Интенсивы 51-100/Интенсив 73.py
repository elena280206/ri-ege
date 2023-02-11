def number(x, y):
    alf = '0123456789abcd'
    return int(f'{alf[x]}231{alf[y]}', 12) + int(f'78{alf[x]}98{alf[y]}', 14)

for i in range(14):
    n = number(i)
    if n % 99 == 0:
        print(n // 99)
        break
