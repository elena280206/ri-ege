x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
deltX = abs(x2 - x1)
deltY = abs(y2 - y1)
if deltX == 2 and deltY == 1 or deltX == 1 and deltY == 2:
    print('YES')
else:
    print('NO')
