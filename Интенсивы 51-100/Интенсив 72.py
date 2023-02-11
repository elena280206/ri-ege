n = [int(input()) for i in input().split(' ')]
count = 0
for d in n:
    for z in n:
        if (d % 2 != z % 2) and ((d // 10) - (d % 10)*2) % 7 == 0 or ((z // 10) - (z % 10)*2) % 7 == 0:
            count += 1
print(count)