n = [int(i) for i in open('file.txt').read().splitlines()]
count = []

def five(x):
    s = ''
    while x > 0 :
        s = str(x % 5) + s
        x //= 5
    return(x)

def dell(x):
    if x % 31 == 0 or x % 47 == 0 or x % 53 == 0:
        return True
def three(x):
    s = ''
    while x > 0 :
        s = str(x % 3) + s
        x //= 3
    return(x)

for i in range(len(n)):
    if five(n[i]) % 5 == three(n[i]) % 3:
        if dell(n[i]) == True:
            count.append(n[i])
print(len(count), min(count))