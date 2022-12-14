n = int(input())
x1 = 0
x2 = 0
m = 0
b = len('n')
b1 = int(b)
while n != 0:
    x1 = n % 10
    x2 = (n // 10) % 10
    if x1 < x2:
        m += 1
    n = n // 10
if m == b1 - 1:
    print('YES')
else:
    print('NO')
