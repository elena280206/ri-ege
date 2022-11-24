n = int(input())
z = 0
l = n
while n > 0:
if (n % 10) % 2 == 1:
    if n // 10 == 0:
        break
    if ((n // 10) % 10) % 2 == 0: