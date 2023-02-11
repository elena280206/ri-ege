line = input().split()
m = n = 0
for i in range(len(line)):
    if (line[i] == 'A' and i % 2 == 0) or (line[i] == 'B' and i % 2 == 1):
        m += 1
        n = max(n, m)
print(n // 2)