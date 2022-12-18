n = input()
r = input()
print(n.count(r)) #Столько раз r встречается в n
if n.count(r) > 0:
    print(n.find(r), n.rfind(r)) #индексы первого и последнего вхождений r в n
else:
    print('Вхожденй нет') #если вхождений r в n нет
print(n.replace(r, 'ЗАМЕНА')) #замена r в n на другую строку