n = input()
k = 1
kmax = 0
for i in range(0, int(len(n))):
    if n[i] in n == n[i + 1] in n:
        k += 1
        kmax = max(k, kmax)
    else:
        k = 1
print(kmax)