n = int(input())
s = 0
max1 = s
max2 = 0
max3 = 0
for i in range(1, int((n**0.5)+1)):
    if n % i == 0:
        s += i
        print(s)
        s += n // i
        print(s)
        #if max2 > max1
           # max2 = s
print(s)