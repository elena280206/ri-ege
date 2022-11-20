n = int(input())
i = n % 10
while n >= 100:
    n = n // 10
j = n // 10
print(min(i, j))
print(max(i, j))