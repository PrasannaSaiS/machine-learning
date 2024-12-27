
import numpy as np
import pandas as pd
data=pd.DataFrame(data= pd.read_csv('Documents/enjoysport.csv'))
print(data)



concept=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])
print(target)
print(concept)


def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("Initialization of specific_h and general_h")
    general_h= [["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
    print("general_h: ", general_h)
    print("concepts: ", concepts)
    for i, h in enumerate(concepts):
        if target[i]=="yes":
            for x in range(len(specific_h)):
                
                if h[x]!= specific_h[x]:
                    specific_h[x]="?"
                    general_h[x][x]='?'
        if target[i]=="no":
            for x in range(len(specific_h[x])):
                if h[x]!= specific_h[x]:
                    general_h[x][x]= specific_h[x]
            else:
                general_h[x][x]="?"
    print("\nSteps of Candidate Elimination Algorithm",i+1)
    print("specific_h: ",i+1)
    print(specific_h,"\n")
    print(general_h)
    indices= [i for i, val in enumerate(general_h) if val==['?','?','?','?','?','?']]
    print("\nIndices", indices)
    
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h, general_h



s_final,g_final= learn(concept, target)
print("\nFinal Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")

