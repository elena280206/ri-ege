a = [int(i) for i in open('1.txt').read().splitlines()]
n = len(a)
pairs = []
count = 0
srcount = 0
for j in range(n):
    if j % 2 == 0:
        srcount += j
srcount = srcount / n
for i in range(n):
    if a[i] % 3 == 0 and a[i + 1] < srcount:
        pairs.append(a[i] + a[i + 1])
print(len(pairs), max(pairs))