m = []
count = 0
for i in range(1, 1001):
    for j in range(1, (int(i**0.5)+1)):
        if i % j == 0:
            count += 1
    if count == 1:
        m.append(i)
    count = 0
print(m)