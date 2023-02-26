#12*45*
for i in range(0, 1000000):
    if str(i)[:2] == '12' and '45' in str(i) and i % 51 == 0:
        print(i, i // 51)