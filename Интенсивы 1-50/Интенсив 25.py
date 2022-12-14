a = int(input())
b = int(input())
num = 0
for i in range(a, b+1):
    if i % 10 == 4 or i % 10 == 9:
        num = num + 1
print(num)