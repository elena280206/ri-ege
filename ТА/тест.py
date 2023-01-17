a = [int(input()) for i in range(int(input()))]
b = []
summ = 0
summax = 0
for i in a:
    if i % 3 == 0:
        b.append(i)
for i in range(len(b) + 1):
    summ = i + (i + 1)
    if summax <= summ:
        summax = summ
print((len(b) // 2), end= ' ')
print(b)