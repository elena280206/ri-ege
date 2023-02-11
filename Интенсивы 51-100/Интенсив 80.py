a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)
pairs = []
count = 0
for i in range(n - 1):
    if (a[i] % 10 == 6 and a[i] % 3 == 0) or (a[i + 1] % 10 == 6 and a[i + 1] % 3 == 0):
        count += 1
        pairs.append((min(a[i], a[i + 1])))
print(count, min(pairs))