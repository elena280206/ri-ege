k = 0
for x1 in 'комбайн':
    for x2 in 'комбайн':
        for x3 in 'комбайн':
            for x4 in 'комбайн':
                for x5 in 'комбайн':
                    for x6 in 'комбайн':
                        for x7 in 'комбайн':
                            s = x1 + x2 + x3 + x4 + x5 + x6 + x7
                            if x1 != 'й' and s.count('ай') == 0:
                                k += 1
print(k)