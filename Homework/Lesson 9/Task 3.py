a = input()
b = input()
c = input()
if len(a) == min((len(a)), len(b), len(c)):
    print(a)
if len(b) == min((len(a)), len(b), len(c)):
    print(b)
if len(c) == min((len(a)), len(b), len(c)):
    print(c)
if len(a) == max((len(a)), len(b), len(c)):
    print(a)
if len(b) == max((len(a)), len(b), len(c)):
    print(b)
if len(c) == max((len(a)), len(b), len(c)):
    print(c)