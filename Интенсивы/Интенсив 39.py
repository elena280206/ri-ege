for i in range(25, 36):
    while i != 1:
        if i % 2 == 1:
            i = (i * 3 + 1) / 2
            print(i)
        else:
            i = i / 2
            print(i)