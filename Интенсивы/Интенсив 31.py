n = int(input())
summ = 0
multiply = 1
for i in range(0, n):
    a = int(input())
    if a % 2 == 1:
        multiply = multiply * a
    else:
        summ += a
g = max(summ, multiply) / min(summ, multiply)
print(g)