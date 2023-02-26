m = open('file.txt').read()
count = 1
maximal = 0
for i in range(1, len(m)):
    if m[i - 1] == 'X' and m[i] == 'X':
        count += 1
        if count > maximal:
            maximal = count
    else:
        count = 1
print(maximal)