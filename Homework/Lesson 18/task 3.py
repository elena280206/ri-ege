n = input()
n1 = int(len(n))
l = 0
for i in range(0, n1 - 1):
    if n[i] == n[i + 1]:
        l += 1
print(l)