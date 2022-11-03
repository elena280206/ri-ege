a1 = input()
b1 = input()
c1 = input()
a = len(a1)
b = len(b1)
c = len(c1)
if a < b and c:
    print(a1, 'самое короткое название')
elif b < c and a:
    print(b1, 'самое короткое название')
elif c < a and b:
    print(c1, 'самое короткое название')
if a > b and c:
    print(a1, 'самое длинное название')
elif b > c and a:
    print(b1, 'самое длинное название')
elif c > a and b:
    print(c1, 'самое длинное название')
