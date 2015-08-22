######The Main Program for Uidclc Parameter.





#### Inputfunc Module
##   Test Version
def inputfunc(filename):
    data=[]
    
    file=open(filename,encoding='utf-8')
    dataclc=file.readlines(5000)
    
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
### clcdata={'uid':['uid',[0,0,0],[0,0,0]...}
def UIDCLC(uidt):
    
    uidclc={}
    
    for i in uidt:
        clc=[i,[0,0,0],[0,0,0]]
        uidclc[i]=clc
 
    return uidclc   ####uidclc container





#### UIDforward data process function.
##   Input data structrue is ['uid','mid','0000-00-00','0','0','0','content']
##                     uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
##   get an output: uidfd={'uid':['uid','uidhttpf',['http1','http2'...],['f1',...]],...]}
def UIDhttp(data):
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

            httpf=[]
            httpc=[]
            httpl=[]
            

            uidfd[uidf[0]]=[uidf[0],'uidhttpf',[],[]]
            uidcd[uidc[0]]=[uidc[0],'uidhttpc',[],[]]
            uidld[uidl[0]]=[uidl[0],'uidhttpl',[],[]]

            if 'http:' in i[6]:
                uidfd[uidf[0]][2].append(i[3])     ##uidf=['uid',i[3]]
                uidcd[uidc[0]][2].append(i[4])
                uidld[uidl[0]][2].append(i[5])
            else:
                uidfd[uidf[0]][3].append(i[3])     ##uidf=['uid',i[3]]
                uidcd[uidc[0]][3].append(i[4])
                uidld[uidl[0]][3].append(i[5])

        elif uidf[0]==i[0]:
            if 'http:' in i[6]:
                uidfd[uidf[0]][2].append(i[3])     ##uidf=['uid',i[3]]
                uidcd[uidc[0]][2].append(i[4])
                uidld[uidl[0]][2].append(i[5])
            else:
                uidfd[uidf[0]][3].append(i[3])     ##uidf=['uid',i[3]]
                uidcd[uidc[0]][3].append(i[4])
                uidld[uidl[0]][3].append(i[5])


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
        (int(li) for li in i) 
        ic=ic+1

    return il



#### Median Function

def MedianFunc(ilist):
    sl=ilist
    sl.sort()
    print(sl)

    mn=len(sl)//2
    print(mn)

    if len(sl)==0:
        median=0
    else:
        median=sl[mn]

    return median



####Forward dic function.

def forwardclc(uidt):
    forwardclc={}

    for i in uidt:
        clc=[i,0,0,0]
        forwardclc[i]=clc

    return forwardclc






#### Main
###  Input: dsfdata(uidfd,uidcd,uidld);uidtable;clcdata;
###         uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
###         uidtable=['uid1',...'uidn']
###         clcdata={'uid':['uid',0,0,0],...}

##  Dev.   /// filt the large one and the 

filename='D:\AliBigDate\weibo_train_data\weibo_train_data.txt'
data=inputfunc(filename)
uidt=uidtable(data)
uidclc=UIDCLC(uidt)
dsf=UIDhttp(data)



##with open('D:\AliBigDate\weibo_train_data\outfile.txt','w',encoding='utf-8') as outfile:
##    out=outfile
##    for i in uidt:
##        out.write('{0}\n{1}\n\n'.format(dsf[1][i],fdsf[1][i]))



####个性化HTTP影响评价，根据中位数/平均值判断





for uid in uidt:
##    mnsn=2
    
    mdataf=dsf[0][uid]
    mdatac=dsf[1][uid]
    mdatal=dsf[2][uid]

##    cf0=mdataf.count('0')
##    cc0=mdatac.count('0')
##    cl0=mdatal.count('0')

##    lnf=len(mdataf)-mnsn
##    lnc=len(mdatac)-mnsn
##    lnl=len(mdatal)-mnsn

##    bf=cf0/lnf       ## zero Frequency
##    bc=cc0/lnc
##    bl=cl0/lnl

    af=0             ## average _INIT_
    ac=0
    al=0

    fl=0.5           ## filter line
    fpara=0.5
    cpara=0.5
    lpara=0.5



##### Filt the outstand items.
    

    df=S2I(mdataf[2:])

    afhttp=MedianFunc(df[0])
    afnhttp=MedianFunc(df[1])

    uidclc[uid][1][0]=afhttp
    uidclc[uid][2][0]=afnhttp
    



##coment
    
    dc=S2I(mdatac[2:])

    achttp=MedianFunc(dc[0])
    acnhttp=MedianFunc(dc[1])
               
    uidclc[uid][1][1]=achttp
    uidclc[uid][2][1]=acnhttp



##like

    dl=S2I(mdatal[2:])

    alhttp=MedianFunc(dl[0])
    alnhttp=MedianFunc(dl[1])
        
    uidclc[uid][1][2]=alhttp
    uidclc[uid][2][2]=alnhttp

#################################################



    






####pdata module///####uidclc outfile module
        
        
pdata=inputfunc('/home/s42/AliBigDate/weibo_predict_data/weibo_predict_data.txt')



outfile=open('/home/s42/AliBigDate/outfile','w')


for i in pdata:
    try:
        if 'http:' in i[3]:
            outfile.write('{0}\t{1}\t{2},{3},{4}\n'
                      .format(str(uidclc[i[0]][0]),str(i[1]),str(uidclc[i[0]][1][0]),
                              str(uidclc[i[0]][1][1]),str(uidclc[i[0]][1][2])))
        else:
            outfile.write('{0}\t{1}\t{2},{3},{4}\n'
                      .format(str(uidclc[i[0]][0]),str(i[1]),str(uidclc[i[0]][2][0]),
                              str(uidclc[i[0]][2][1]),str(uidclc[i[0]][2][2])))

    except:
        outfile.write('{0}\t{1}\t{2},{3},{4}\n'.format(i[0],i[1],'0','0','0'))
        

outfile.close()









