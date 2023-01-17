a = int(input())
b = int(input())
c = int(input())
x = ''
discr = b**2 - 4*a*c
if discr > 0:
    x1 = (float(-b + discr**0.5) / (2 * a))
    x2 = (float(-b - discr**0.5) / (2 * a))
    print(min(x1, x2), max(x1, x2))
elif discr == 0:
    print(-b / 2*a)
elif discr < 0:
    print('Нет корней')