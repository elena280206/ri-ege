a = int(input())
n = a // 1000
if n >= 1 and a % 7 == 0 or a % 17 == 0:
    print('YES')
else:
    print('NO')