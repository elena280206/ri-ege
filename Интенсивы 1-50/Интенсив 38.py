n = int(input())
g = str(n)
i = ''
while n > 0:
    i += str(n % 10)
    n = n // 10
if i == g:
    print('YES')
else:
    print('NO')