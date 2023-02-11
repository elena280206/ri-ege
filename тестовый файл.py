a = int(bin(4**2014 + 2**2015 - 8)[2:])
count = 0
m = ''
while a != 0:
    m = a % 2
    if m == 1:
        count += 1
    m = ''
    a //= 2
print(count)