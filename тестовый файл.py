from random import shuffle

def alg:
    while '111' in st or '222' in st:
        if '111' in st:
            st = st.replace('111', '22', 1)
        else:
            st = st.replace('222', '11', 1)
    return(st)

s = list(('3'*70 + '2'))
shuffle(s)
s = str(s)
st = ''.join(s)
new = alg(new)
print(new)