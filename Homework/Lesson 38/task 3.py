c = 0
m = 0
simv = ''
for i in range(120115, 120200):
    for j in range(2, int((i**0.5) + 1)):
        if i % j == 0:
            c += 1
        if c >= m:
            m = c
            simv = i
    c = 0
print(simv, m)