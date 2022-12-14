summ = 0
count = 0
n = int(input())
for i in range(0, n):
    a = int(input())
    m = a / 100
    if a % 2 == 1 and 1 <= m < 10:
        summ += a
        count += 1
print(summ / count)