a = open('1.txt').read()
count = 1
p = []
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        count += 1
    else:
        p.append(count)
        count = 1
print(p.count(5))