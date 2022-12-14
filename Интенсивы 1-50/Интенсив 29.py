n = int(input())
mx1 = mx2 = mx3 = 0
for i in range(n):
    b = int(input())
    if i != 0:
        if mx1 < b:
            mx2 = mx1
            mx1 = b
            if mx3 < mx2:
                mx3 = mx2
                mx2 = mx1
print(mx1, mx2, mx3)
