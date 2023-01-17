n = int(input())
a = []
count = 0
m = 0
for i in range(2, n + 1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            count += 1
            m = count
            if m >= 2:
                a.append(i)
                count = 0
print(a)