
HOT_HIDDEN=[0.2,0.4,0.4]
COLD_HIDDEN=[0.5,0.4,0.1]
HOT=[0.7,0.3]
COLD=[0.4,0.6]

hotSeries=[]
coldSeries=[]

hotPath=["HOT"]
coldPath=["COLD"]

pos1Hot=0.8*HOT_HIDDEN[2]
hotSeries.append(pos1Hot)

pos1Cold=0.2*COLD_HIDDEN[2]
coldSeries.append(pos1Cold)

O=[2,0,0,1,1,2,0,2]

for i in range(8):
    o1=O[i]
    hot_temp1=hotSeries[i]*HOT[0]*HOT_HIDDEN[o1]
    hot_temp2=coldSeries[i]*COLD[0]*HOT_HIDDEN[o1]
    if (hot_temp1>hot_temp2):
        temp1=hot_temp1
        hotSeries.append(temp1)
        hotPath.append("HOT")
    else:
        temp1=hot_temp2
        hotSeries.append(temp1)
        hotPath.append("COLD")

    cold_temp1=hotSeries[i]*HOT[1]*COLD_HIDDEN[o1]
    cold_temp2=coldSeries[i]*COLD[1]*COLD_HIDDEN[o1]
    if (cold_temp1>cold_temp2):
        temp1=cold_temp1
        coldSeries.append(temp1)
        coldPath.append("HOT")
    else:
        temp1=cold_temp2
        coldSeries.append(temp1)
        coldPath.append("COLD")
    
#print(hotSeries)
#print(coldSeries)
#print(hotPath)
#print(coldPath)

max1=0.0
PATH=[]
if (hotSeries[8]>coldSeries[8]):
    max1=hotSeries[8]
    PATH.append(hotPath[8])
    step=hotPath[8]
    for i in range(8):              
        if (step=="HOT"):
            PATH.append("HOT")
            step=hotPath[7-i]
        else:
            PATH.append("COLD")
            step=coldPath[7-i]

else:
    max1=coldSeries[8]
    PATH.append(coldPath[8])
    for i in range(9):
        temp1=coldPath[8-i]        
        if (temp1=="HOT"):
            temp2=hotPath[7-i]
        else:
            temp2=coldPath[7-i]

        PATH.append(temp2)

new_PATH=[]

for i in range(9):
    temp1=PATH[8-i]
    new_PATH.append(temp1)
            
#print(max1)
#print(new_PATH)

print("The most likely path for 331122313 is: "+str(new_PATH))
print("The total likelihood is: "+str(max1))

