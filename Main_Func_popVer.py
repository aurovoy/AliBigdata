######The Main Program for Uidclc Parameter.





#### Inputfunc Module
##   Test Version
def inputfunc(filename):
    data=[]
    
    file=open(filename,encoding='utf-8')
    dataclc=file.readlines(1000000)
    
    for i in dataclc:
        data.append(i.split('\t'))   ###datecollect.process
     
    file.close()

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
 
    return uidclc   ####uidclc container






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



#### Filter
def ffunc(nlist):
    sl=nlist
    sl.sort()

    lsl=1+len(sl)//10

    for i in range(int(lsl)):
        sl.pop()
        
    return sl
    



#### str to int, for the list
def S2I(ilist):
    ic=0
    il=ilist
    for i in il[:]:
        il[ic]=int(i)
        ic=ic+1

    return il





#### Main
###  Input: dsfdata(uidfd,uidcd,uidld);uidtable;clcdata;
###         uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
###         uidtable=['uid1',...'uidn']
###         clcdata={'uid':['uid',0,0,0],...}

##  Dev.   /// filt the large one and the 

filename='\weibo_train_data.txt'
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

    fl=0.5           ## filter line
    fpara=0.5
    cpara=0
    lpara=0



##### Filt the outstand items.
    
    if bf>=fl:
        uidclc[uid][1]=0
    elif bf<fl:
        df=S2I(mdataf[2:])
        lsdf=1+len(df)//10

        sdf=ffunc(df)           #poplist

        if len(sdf)==0:         #avoid one item list
            af=sum(df)

        else:
            ssdf=sum(sdf)
            af=ssdf/(lnf-lsdf)
        
        uidclc[uid][1]=round(af)


    if bc>=fl:
        uidclc[uid][2]=0
    elif bc<fl:
        dc=S2I(mdatac[2:])
        lsdc=1+len(dc)//10

        sdc=ffunc(dc)

        if len(sdc)==0:
            ac=sum(dc)

        else:
            ssdc=sum(sdc)
            ac=ssdc/(lnc-lsdc)
               
        uidclc[uid][2]=round(ac)


    if bl>=fl:
        uidclc[uid][3]=0
    elif bl<fl:
        dl=S2I(mdatal[2:])
        lsdl=1+len(dl)//10

        sdl=ffunc(dl)

        if len(sdl)==0:
            al=sum(dl)

        else:
            ssdl=sum(sdl)
            al=ssdl/(lnl-lsdl)
        
        uidclc[uid][3]=round(al)

#################################################



####pdata module///####uidclc outfile module
        
        
pdata=inputfunc('')



outfile=open('/outfile','w')


for i in pdata:
    if i[0] not in uidt:
        outfile.write('{0}\t{1}\t{2},{3},{4}\n'.format(i[0],i[1],'0','0','0'))

    else:
    
        outfile.write('{0}\t{1}\t{2},{3},{4}\n'.format(str(uidclc[i[0]][0]),str(i[1]),str(uidclc[i[0]][1]),str(uidclc[i[0]][2]),str(uidclc[i[0]][3])))

outfile.close()







