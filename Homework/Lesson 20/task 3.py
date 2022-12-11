n = input()
m = int(len(n))
j = n
g = m
while n != '':
    if n[-1:] == 'p':
        n = n[:-1]
        m -= 1
        break
    m -= 1
    n = n[:-1]
l = j[m + 1:]
n = j[m:]
while n != '':
    if n[-1:] == 'p':
        n = n[:-1]
        m -= 1
        break
    m -= 1
    n = n[:-1]
i = j[: m - 1]
print(f'{i}{l}')