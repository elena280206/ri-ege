strr = input()
bukv = ''.join(c for c in strr if c.isalpha())
cifr = ''.join(j for j in strr if j.isdigit())
zagl = 0
chet = 0
angl = 0
for i in bukv:
    if i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЁЮ':
        zagl += 1
    elif i in 'qwertyuioplkjhgfdsazxcvbnm':
        angl += 1
for m in cifr:
    if m in '02468':
        chet += 1
print(zagl, angl, chet)