m = 0
for i in range(2422000, 2422081):
    co = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            co += 1
    if co == 0:
        m += 1
        print(m, i)
