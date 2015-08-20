#### str to int, for the list


def S2I(ilist):
    i=0
    il=ilist
    for i in il[:]:
        il[i]=int(i)
        i=i+1

    return il
