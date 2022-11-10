n = int(input())
sumDev = 0
for i in range(1, n + 1):
    if n % i == 0:
        sumDev = sumDev + i
print(sumDev)
