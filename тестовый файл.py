numb = int(input())
for i in reversed(range(numb - 1, 1)):
    simple = 0
    if numb % i == 0:
        for m in reversed(range(i - 1, 1)):
            if i % m == 0:
                simple = simple + 1
            print(i)