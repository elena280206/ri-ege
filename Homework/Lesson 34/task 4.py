a = [int(i) for i in open('dz.txt').read().splitlines()]
p = []
massiv = []
for i in range(len(a)):
    if a[i] % 100 == 52:
        massiv.append(a[i])
razn = max(massiv) - min(massiv)
for i in range(len(a) - 1):
    if (a[i] < razn and a[i + 1] >= razn) or (a[i] >= razn and a[i + 1] < razn):
        p.append(a[i] + a[i + 1])
print(len(p), max(p))