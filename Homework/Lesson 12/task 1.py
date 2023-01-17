n = int(input())
max1 = max2 =1
print(0, max1, max2, end= ' ')
for i in range(3, n):
    max1, max2 = max2, max1 + max2
    print(max2, end= ' ')