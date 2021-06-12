import math

def Shannonindex(Occurance_rate):    
    index = []
    for i in range (0,len(Occurance_rate)):
        x = Occurance_rate[i]
        p = -1 * (x * math.log(x)) 
        index.append(p)
     
    
    Sindex = sum(index)
    return Sindex
