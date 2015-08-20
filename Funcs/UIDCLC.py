####UID Collect Module.
## OUTPUT: uidclc={'uid':['uid',0,0,0],...}

def UIDCLC(data):
    initUID=0
    
    uidclc={}
    
    for i in data:
        if i[0]!=initUID:
            clc=['uid',0,0,0]
            initUID=i[0]
            clc[0]=initUID
            
            uidclc[i[0]]=clc
            
        elif i[0]==initUID:
            pass

    
    return uidclc   ####包含空值的uidclc?
