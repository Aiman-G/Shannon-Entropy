# Aymen.omg@gmail.com

import math

def Shannonindex(Occurance_rate):    
    index = []
    for i in range (0,len(Occurance_rate)):
        x = Occurance_rate[i]
        p = -1 * (x * math.log(x)) 
        index.append(p)
     
    
    Sindex = sum(index)
    return Sindex

# Example of population ;
pop=[[1,2,3,9,15,20],[1,2,3,8,14,20],[1,2,3,4,10,15,20]] ## population are paths from a graph
# These paths are sampled from path between a pair of source and destination in  a graph. So each path starts and terminate with the same source and destination 

def Occurance_rate_func(pop,g): # g is a networkx graph
    UniversalSet=g.nodes()
    UniversalSet=list(UniversalSet)
    UniversalSet.remove(src)    # remove src and dst , they are repeated in every path
    UniversalSet.remove(dst)
    
    all_Occurrence_dic={}
    all_Occurrence=[]
    gene_Occurrence=0
   
    for k in range (0, len(UniversalSet)):
    
        gene_inU=UniversalSet[k]
        gene_Occurrence=0
        for i in range (0,len(pop)):

            p=pop[i]
            p=p[1:-1]

            # Remember : we should remove source and destintion nodes form the universal set too

            gene_Occurrence= gene_Occurrence+p.count(gene_inU)

            all_Occurrence_dic.update({gene_inU:gene_Occurrence})

    
    
    non_zero_values=[]

    all_vlause= all_Occurrence_dic.values()

    Genes_Occurrence_rate=[]

    non_zero_values=[]


    for value in all_Occurrence_dic.values():
        if value!=0:
               
            non_zero_values.append(value)
            
    Genes_Occurrence_rate=[x /len(pop) for x in non_zero_values] # or non_zero_values
    
    #___________________
    
    Genes_occurance_rate_No_Ones = [x for x in Genes_Occurrence_rate if x != 1]# remove ones
    
    Shanon_index = Shannonindex(Genes_occurance_rate_No_Ones) # shanon index
    
    
    n=len(pop)
    Log_of_n=math.log(n)
    
    Shannon_of_restTerms=Shannonindex(Genes_occurance_rate_No_Ones[n:]) 
    Normalized_Shannon=Shanon_index/(Shannon_of_restTerms+math.log(n))
    
    return Normalized_Shannon


# to get a sample of the pop
You need Networkx, to generate a graph. 


def get_sample(g,src,dst):
  
    number_of_paths=0
    SomePaths=[]
    for path in nx.all_simple_paths(g, source=src, target=dst): # provide your graph, and a pair of source and destination 
        number_of_paths=number_of_paths+1
        SomePaths.append(path)
        if number_of_paths== Some_number:
            break
  return SomePaths

            
     
                                    

    
