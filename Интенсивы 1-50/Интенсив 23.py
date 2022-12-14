str1 = len(input())
str2 = len(input())
str3 = len(input())
if max(str1, str2, str3) - ((max(str1, str2, str3) + min(str1, str2, str3)) / 2) \
        == ((max(str1, str2, str3) + min(str1, str2, str3)) / 2) - min(str1, str2, str3):
    print('YES')
else:
    print('NO')