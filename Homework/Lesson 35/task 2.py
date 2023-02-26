a = [int(i) for i in open('dz.txt').read().splitlines()]
p = []
for i in range(9999):
    if (a[i] - a[i + 1]) % 2 == 0 and (a[i] % 31 == 0 or a[i + 1] % 31 == 0):
        p.append(a[i] + a[i + 1])
print(max(p))
