count = []
alf = '0123456789a'
for x in alf:
    for y in alf:
        a = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        if a % 305 == 0:
            count.append(a)
print(min(count) // 305)