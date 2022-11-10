m = int(input())
p = int(input())
n = int(input())
p = p / 100
for i in range(1, n + 1):
    m = m + m * p
    print(m)
