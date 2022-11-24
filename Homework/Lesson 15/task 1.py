i = ''
l = ''
z = ''
for n in range(10, 1001):
    g = n
    n = bin(n)
    n = ((n)[2:])
    n = int(n)
    while n > 0:
        m = str(n % 10)
        i = str(i) + m
        n = n // 10
    i = int(i) // 10
    while i % 2 == 0:
        i = i // 10
    while int(i) > 0:
        z = str(i % 10)
        l = z + z
        i = i // 10
    l = int(l, 2)
    summ = g - l
    print(summ)