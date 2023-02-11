a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)
sums = []

min21 = min([i for i in a if i % 21 == 0])

def sun8(x):
    x = oct(x)[2:]
    s = sum([int(i) for i in x])
    return(s)

for i in range(n - 1):
    if sun8(a[i]) == sun8(min21) or sun8(a[i + 1]) == sun8(min21):
        sums.append(a[i] + a[i + 1])
print(len(sums), min(sums))