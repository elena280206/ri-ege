def M(x):
    alf = '0123456789abcd'
    return int(f'8{x}12{x}', 14)

def N(x):
    alf = '0123456789abcd'
    return int(f'8{x}542', 14)

flag = False
for A in range(1, 1000):
    if flag:
        break
    for x in range(14):
        if (M(x)+A) % N(x) == 0:
            print(A)
            flag = True
            break