
def find_floor(f1, secret):
    Dn = []
    step = 1
    while f1 - step >0:
        Dn.append(f1-step)
        f1-= step
        step+=1
    Dn.reverse()
    attempt = 0
    print(Dn)
    for i in range(len(Dn)):
        attempt+=1
        if Dn[i] == secret:
            return (attempt, Dn[i])
        if Dn[i] > secret:
            start = Dn[i-1] if i else 0
            for j in range(start+1, Dn[i]):
                attempt+=1
                if j == secret:
                    return (attempt, j)
    return (attempt+1, Dn[-1]+ 1)


find_floor(200, 46)
