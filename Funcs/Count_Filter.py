#### Filter

def ffunc(nlist):
    sl=nlist
    sl.sort()

    lsl=1+len(sl)//10

    for i in range(int(lsl)):
        sl.pop()
        
    return sl
