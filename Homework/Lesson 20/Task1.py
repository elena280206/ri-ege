line = input()
n = (len(line) + 2) // 2
str1 = line[: n - 1]
str2 = line[n - 1:]
print(str2 + str1)