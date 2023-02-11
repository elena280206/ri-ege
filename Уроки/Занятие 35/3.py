a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)

def fullM(i1, n1):
    return i1**(1/3) == int(i1**(1/n1))



M = max([i for i in a if fullM(i, 3)])
p_pr = []
p_sum = []
for i in range(n-2):
    three = a[i:i+3]
    d = abs(M - sum(a[i:i+3]))
    if fullM(d, 2)  and d % 2 == 0:
        t = sorted(three)
        p_pr.append([t[0]*t[1], sum(t)])
        p_sum.append(sum(t))
print(len(p_pr), p_pr