#### Inputfunc Module

def inputfunc(filename):
    dataCLC=[]
    
    file=open(filename,encoding='utf-8')
    
    for i in range(20):
        datacollect=file.readline()
        dataCLC.append(datacollect.split('\t'))   ###datecollect.process
     
    file.close()
    
    return dataCLC
