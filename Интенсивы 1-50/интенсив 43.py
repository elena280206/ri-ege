n = int(input())
m = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(m + 1, end = '')
        m += 1
    print()
