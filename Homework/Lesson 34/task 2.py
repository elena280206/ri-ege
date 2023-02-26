a = [int(i) for i in open('dz.txt').read().splitlines()]
p = []
for i in range(len(a) - 2):
    if 0 < a[i + 1] % 100 < 10 and a[i + 1] % 10 == 5:
        p.append(a[i] + a[i + 1] + a[i + 2])
print(len(p), max(p))