str1 = input()
str1 = str1[::-1]
str2 = ''
str3 = ''
for i in range(int(len(str1))):
    if i % 2 == 0:
        str2 += str(str1[-1:])
    else:
        str3 += str(str1[-1:])
    str1 = str1[:-1]
print(str2, str3)