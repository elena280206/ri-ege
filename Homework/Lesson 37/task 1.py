a = open('1.txt').readline()
c = 0
for i in a:
    if i.count('U') < i.count('K'):
        c += 1
print(c)