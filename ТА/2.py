a = []
for x in range(10, 1000):
    m = int(format(x, 'b'))
    m = str(m)[1:]
    for i in str(m):
        while i == 0:
            m = m[1:]
    m = int(m)
    m = format(m, 'x')
    print(x - int(m))