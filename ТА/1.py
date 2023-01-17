strr = '>' + '1' * 10 + '2' * 20 + '3' * 30
while ('>1' in strr) or ('>2' in strr) or ('>3' in strr):
    if '>1' in strr:
        strr = strr.replace('>1', '22>', 1)
    if '>2' in strr:
        strr = strr.replace('>2', '2>', 1)
    if '>3' in strr:
        strr = strr.replace('>3', '1>', 1)
print(strr.count('1') + strr.count('2')*2)