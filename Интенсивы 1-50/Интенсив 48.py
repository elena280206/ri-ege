n = input()
simv = 0
for i in range(int(len(n))):
    if n[-1:] == ' ':
        simv += 1
    n = n[:-1]
print(simv + 1)