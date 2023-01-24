# fio = input().split()
# for i in fio:
#     print(i[0] + '.', end= ' ')
print(*[i[0]+'.' for i in input().split()])
