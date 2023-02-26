d = open('file.txt').read()
count = 1
m = 0
for i in range(1, len(d)):
    if d[i - 1] != d[i]:
        count += 1
        m = max(m, count)
    else:
        count = 1
print(m)