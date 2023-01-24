n = list(input())
summ = 0
m = ''
while n != []:
    m = n[-1:]
    for i in n:
        if m == list(i):
            print(m, list(i))
            #summ += 1
    del n[-1]
#print(summ)