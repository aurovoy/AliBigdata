####UID data process function.

##Input data structrue is ['uid','mid','0000-00-00','0','0','0','content']



def UIDSF(data):
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
            

            
        
        
        
    
