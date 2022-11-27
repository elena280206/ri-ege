n = int(input())
triangle = ''
for i in range(1, n +1):
    for j in range(i):
        triangle += str(i)
    triangle += '\n'
print(triangle)