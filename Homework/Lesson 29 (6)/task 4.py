num = 0
n = 0
for i in range(200, 1000):
    j = '1' * i
    while '1111' in j:
        j = j.replace('1111', '22', 1)
        j = j.replace('222', '1', 1)
    if num < j.count('1'):
        num = j.count('1')
        n = i
print(n)