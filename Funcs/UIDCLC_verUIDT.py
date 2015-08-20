####UID Collect Module.
## OUTPUT: uidclc={'uid':['uid',0,0,0],...}

def UIDCLC(uidt):
    
    uidclc={}
    
    for i in uidt:
        clc=[i,0,0,0]
        uidclc[i]=clc
 
    return uidclc   ####包含空值的uidclc?
