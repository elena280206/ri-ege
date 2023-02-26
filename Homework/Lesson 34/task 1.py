a = [int(i) for i in open('dz.txt').read().splitlines()]
p = []
for i in range(len(a) - 1):
    if a[i] % 2 == 0 and a[i + 1] % 2 == 1:
        if a[i] % 4 == 0 and a[i + 1] % 11 == 0:
            p.append(a[i] + a[i + 1])
    elif a[i] % 2 == 1 and a[i + 1] % 2 == 0:
        if a[i] % 11 == 0 and a[i + 1] % 4 == 0:
            p.append(a[i] + a[i + 1])
print(len(p), max(p))