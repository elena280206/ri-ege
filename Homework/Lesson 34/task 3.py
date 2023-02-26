a = [int(i) for i in open('dz.txt').read().splitlines()]
n = len(a)
p = []
minp = []
for j in range(n):
    if a[j] % 103 == 0:
        minp.append(a[j])
for i in range(n - 1):
    if (a[i] + a[i + 1]) % 2 == 0:
        if (a[i] - a[i + 1]) % min(minp) == 0:
            p.append(a[i] + a[i + 1])
print(len(p), max(p))