a = [str(i) for i in open('1.txt').read().splitlines()]

def good(x, y):
    i = 0
    if x[i] == y[i]:
        return True
    else:
        if i < 4:
            i += 1

counting = []
minimax = int(min(a)) + int(max(a))
for i in range(len(a) - 2):
    if good(a[i], a[i + 1]) or good(a[i + 1], a[i + 2]):
        if (int(a[i]) + int(a[i + 1]) + int(a[i + 2])) < minimax:
            counting.append((int(a[i]) + int(a[i + 1]) + int(a[i + 2])))
print(len(counting), min(counting))