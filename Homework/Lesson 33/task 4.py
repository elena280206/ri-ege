a = [int(i) for i in open('1.txt').read().splitlines()]
p = []
for i in range(9999):
    if (a[i]*a[i + 1]) % 14 != 0:
        p.append(a[i] + a[i + 1])
print(len(p), max(p))