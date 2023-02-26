def system(x, y):
    s = ''
    while x > 0:
        s = str(x % y) + s
        x //= y
    return(s)
Su = 0
for i in range(2, 11):
    if len(system(622, i)) % 2 == 0:
        Su += i
print(Su)