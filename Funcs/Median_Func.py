#### Median Function


def MedianFunc(ilist):
    sl=ilist
    sl.sort()

    mn=len(sl)//2

    median=sl[mn]

    return median
