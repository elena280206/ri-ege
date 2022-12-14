n = int(input())
m = n % 10
count = 0
l = 0
while n > 0:
    l += 1
    t = n % 10
    if m == t:
        count += 1
    n = (n // 10)
print(l == count)