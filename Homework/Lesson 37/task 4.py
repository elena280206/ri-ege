a = open('1.txt').read()
count = 0
p = []
for i in range((len(a) - 1), 2):
    print(i)
    if isinstance(a[i], str) and isinstance(a[i + 1], int):
        count += 1
    else:
        p.append(count)
        count = 0
#print(max(p))
