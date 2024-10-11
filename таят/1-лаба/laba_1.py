def norm(stroka):
    new_str = ''
    for i in stroka:
        if i.isdigit():
            new_str += new_str[-1] * (int(i) - 1)
            continue
        new_str += i
    return new_str


b = '(([])))2'
c = '(2[])3'
d = norm(b)
e = norm(c)
print(d[::-1])
print(d)
print(e)
print(d == e)
