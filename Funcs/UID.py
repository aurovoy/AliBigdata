####UID table


def uidtable(data):
    initUID='uid'

    uidt=[]

    for i in data:
        if i[0]!=initUID:
            uidt.append(i[0])
            initUID=i[0]
            

        elif i[0]==initUID:
            pass
            

    return uidt
