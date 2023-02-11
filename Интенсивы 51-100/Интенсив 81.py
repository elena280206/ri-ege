a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)
pairs = []
count = 0
for i in range(n-3):
    if (a[i] % 2 == 0 and a[i + 2] % 2 == 1) and (a[i + 1] % 2 == 1 and a[i + 3] % 2 == 0):
        count += 1
    elif (a[i] % 2 == 1 and a[i + 2] % 2 == 0) and (a[i + 1] % 2 == 0 and a[i + 3] % 2 == 1):
        count += 1
print(count)