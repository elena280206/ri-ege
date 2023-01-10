n = input()
s = {"i", "e", "u", "o", "a", "y"}
count = -1
for i in n:
    count += 1
    if i == s and i[count + 1] != s or i != s and i[count + 1] == s:
        print('YES')
    else:
        print('NO')
