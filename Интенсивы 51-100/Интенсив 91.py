z = open('1.txt').read()
mcount = 1
counting = 1
for i in range(len(z) - 1):
    if z[i] == z[i + 1]:
        counting += 1
        if counting > mcount:
            mcount = counting
            s = z[i]
    else:
        counting = 1
print(mcount, s)