n = input()
j = n
m = int(len(n))
while n != '':
    if n[-1:] == ' ':
        n = n[:-1]
        m -= 1
        break
    m -= 1
    n = n[:-1]
n = j
line1 = n[: m]
line2 = n[m + 1:]
print(line1, line2, sep = '\n')