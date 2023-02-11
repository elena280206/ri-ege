a = [int(i) for i in open('1.txt').read().splitlines()]
n = len(a)
p = []
for i in range(n - 1):
    if (a[i] + a[i + 1]) % 60 == 0:
        if a[i] % 40 == 0 or a[i + 1] % 40 == 0:
            p.append(a[i] + a[i + 1])
print(len(p), max(p))