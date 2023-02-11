import re

n = [input() for i in range(int(input()))]
for m in n:
    m = re.sub(r'\?', '*', m)
    print(m)