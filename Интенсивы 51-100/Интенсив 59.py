strr = input()
if len(strr) > 10:
    print(strr[:6])
else:
    while len(strr) != 12:
        strr = strr + 'o'
    print(strr)