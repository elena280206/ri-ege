n = input()
numb = 0
count = 0
while n != '':
    if n.find(numb + 1) == n.find(numb):
        count += 1
    n = n[-1:]
print(count)