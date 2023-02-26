#12345?6?8
for i in range(123450608, 123459698 + 1):
    if str(i)[:5] == '12345' and str(i)[6] == '6' and str(i)[-1] == '8' \
        and i % 17 == 0:
        print(i, i // 17)
