m = int(input())
n = int(input())
if m % 2 == 1 and n % 2 == 1:
    for i in reversed(range(n, m + 1, 2)):
        print(i)
elif m % 2 == 1 and n % 2 == 0:
    for i in reversed(range(n, m, 2)):
        print(i + 1)
elif m % 2 == 0 and n % 2 == 0:
    for i in reversed(range(n, m, 2)):
        print(i + 1)
elif m % 2 == 0 and n % 2 == 1:
    for i in reversed(range(n, m + 1, 2)):
        print(i)