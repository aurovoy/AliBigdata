######The Main Program for Uidclc Parameter.





#### Inputfunc Module
##   Test Version
def inputfunc(filename):
    data=[]
    
    file=open(filename,encoding='utf-8')
    dataclc=file.readlines()
    
    for i in dataclc:
        data.append(i.split('\t'))   ###datecollect.process
     
    file.close()
    print(data)
    return data


####UID table
def uidtable(data):

    uidt=[]
    initUID='uid'

    for i in data:
        if i[0]!=initUID:
            uidt.append(i[0])
            initUID=i[0]

        elif i[0]==initUID:
            pass
            

    return uidt



### UID Collect Function.
### clcdata={'uid':['uid',0,0,0],...}
def UIDCLC(uidt):
    
    uidclc={}
    
    for i in uidt:
        clc=[i,0,0,0]
        uidclc[i]=clc
 
    return uidclc   ####包含空值的uidclc?


##def UIDCLC(data):
##    initUID=0
##    
##    uidclc={}
##    
##    for i in data:
##        if i[0]!=initUID:
##            clc=['uid',0,0,0]
##            initUID=i[0]
##            clc[0]=initUID
##            
##            uidclc[i[0]]=clc
##            
##        elif i[0]==initUID:
##            pass
##
##    
##    return uidclc   ####包含空值的uidclc?





#### UID data process function.
##   Input data structrue is ['uid','mid','0000-00-00','0','0','0','content']
##                     uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
def UIDDSF(data):
    uidf=['uid']
    uidc=['uid']
    uidl=['uid']
    uidfd={}
    uidcd={}
    uidld={}
    for i in data:         
        
        if uidf[0]!=i[0]:         
            
            uidf[0]=i[0]
            uidc[0]=i[0]
            uidl[0]=i[0]

            uidfd[uidf[0]]=[uidf[0],'uidf']
            uidcd[uidc[0]]=[uidc[0],'uidc']
            uidld[uidl[0]]=[uidl[0],'uidl']
            
            uidfd[uidf[0]].append(i[3])     ##uidf=['uid',i[3]]
            uidcd[uidc[0]].append(i[4])
            uidld[uidl[0]].append(i[5])

        elif uidf[0]==i[0]:
            uidfd[uidf[0]].append(i[3])     ##uidf=['uid',1i[3],...,ni[3]]
            uidcd[uidc[0]].append(i[4])
            uidld[uidl[0]].append(i[5])


    return(uidfd,uidcd,uidld)











#### Main
###  Input: dsfdata(uidfd,uidcd,uidld);uidtable;clcdata;
###         uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
###         uidtable=['uid1',...'uidn']
###         clcdata={'uid':['uid',0,0,0],...}

filename=input('file is:')
data=inputfunc(filename)
uidt=uidtable(data)
uidclc=UIDCLC(uidt)
dsf=UIDDSF(data)


for uid in uidt:
    mnsn=2
    
    mdataf=dsf[0][uid]
    mdatac=dsf[1][uid]
    mdatal=dsf[2][uid]

    cf0=mdataf.count('0')
    cc0=mdatac.count('0')
    cl0=mdatal.count('0')

    lnf=len(mdataf)-mnsn
    lnc=len(mdatac)-mnsn
    lnl=len(mdatal)-mnsn

    bf=cf0/lnf       ## zero Frequency
    bc=cc0/lnc
    bl=cl0/lnl

    af=0             ## average _INIT_
    ac=0
    al=0

    fl=0.6           ## filter line

    if bf>=fl:
        uidclc[uid][1]=0
    elif bf<fl:
        df=mdataf[2:]
        cn=0
        for i in df:
            it=int(i)
            cn=cn+it

        af=cn/lnf
        uidclc[uid][1]=round(af)

    if bc>=fl:
        uidclc[uid][2]=0
    elif bc<fl:
        dc=mdatac[2:]
        cn=0
        for i in dc:
            it=int(i)
            cn=cn+it

        ac=cn/lnc
        uidclc[uid][2]=round(ac)

    if bl>=fl:
        uidclc[uid][3]=0
    elif bl<fl:
        dl=mdatal[2:]
        cn=0
        for i in dl:
            it=int(i)
            cn=cn+it

        al=cn/lnl
        uidclc[uid][3]=round(al)




print(uidclc)
        

        
        








