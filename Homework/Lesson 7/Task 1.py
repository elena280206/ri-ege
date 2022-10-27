a = int(input())
b = int(input())
c = int(input())
if a < (b + c) and b < (c + a) and c < (a + b):
    print('Yes')
else:
    print('No')