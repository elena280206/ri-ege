m = open('file.txt').read()
count = 1
max = 0
for i in range(len(m) - 1):
    if m[i] + m[i + 1] == 'KL' or m[i] + m[i + 1] == 'LK':
        count = 1
    else:
        count += 1
        if count > max:
            max = count
print(max)