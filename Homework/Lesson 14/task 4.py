n = int(input())
i = 0
k = ''
while n > 0:
    i = n % 10
    k += str(i)
    n = n // 10
print(k)
