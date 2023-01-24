a = [int(i) for i in input().split()]
rost = int(input())
count = 0
while count < len(a) and a[count] >= rost:
    count += 1
print(count)