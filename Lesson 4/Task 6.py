a = input()
b = input()
c = input()
if a <= b <= c:
    print(a, b, c)
if a <= c <= b:
    print(a, c, b)
if b <= a <= c:
    print(b, c, a)
if b <= c <= a:
    print(b, c, a)
if c <= b < a:
    print(c, b, a)
if c <= a <= b:
    print(c, a, b)
