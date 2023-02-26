import math

def M(x):
    l = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            l.append(i)
    if l == []:
        return 0
    else:
        return max(l) - min(l)

summa = 0
n = 350000
while summa < 6:
    if M(n) % 23 == 9:
        summa += 1
        print(summa, n)
    n += 1