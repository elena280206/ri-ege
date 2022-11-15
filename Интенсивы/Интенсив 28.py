n = int(input())
max1 = max2 = max3 = 0
for i in range(1, n + 1):
    if n % i == 0:
        i += i
        max1 = i
        print(i)
        i += n // i
        print(i)
        if max1 < i:
            max2 = i
    if max2 < i:
        print(max1, max2, max3)
