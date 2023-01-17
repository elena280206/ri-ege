n = input()
count = 0
for i in n:
    if i == i.lower() and i.isalpha():
        count += 1
print(count)