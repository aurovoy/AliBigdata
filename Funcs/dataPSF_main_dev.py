####UID date process function.
## Count, Sum, Average etc. //
## Input: dsfdata(uidfd,uidcd,uidld);uidtable;clcdata;
###        uidfd={'uid':['uid','uidf','f1','f2',...,'fn'],...}
###        uidtable=['uid1',...'uidn']
###        clcdata={'uid':['uid',0,0,0],...}
## Output for the basic parameter in UIDCLC.


def UIDDPF(uidtable,clcdata,*dsfdata):
    clc=clcdata
    datadsf=dsfdata
    uidt=uidtable

    for uid in uidt:
        mnsn=2
        metadataf=datadsf[0][uid]
        metadatac=datadsf[1][uid]
        metadatal=datadsf[2][uid]
        
        counterf0=metadataf.count('0')
        counterc0=metadatac.count('0')
        counterl0=metadatal.count('0')
        nf=len(metadataf)-mnsn
        nc=len(metadatac)-mnsn
        nl=len(metadatal)-mnsn
        bf=counterf0/nf
        bc=counterc0/nc
        bl=counterl0/nl
        
        aff=0
        afc=0
        afl=0

        if bf>=0.6:
            f=0

        elif bf<0.6:
            df=metadataf[2:]
            cn=0
            for i in df:
                
                
            







        
