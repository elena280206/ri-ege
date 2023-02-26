co = 0
summ = 0
for i in range(2, 20001):
    co = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            co += 1
    if co >= 3:
        summ += 1
print(summ)