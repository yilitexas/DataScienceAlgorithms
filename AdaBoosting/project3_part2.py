import math

input1=open("file2.txt","r")
read1=input1.readlines()
#print(read1)

line1=read1[0].split()
T=int(line1[0])
n=int(line1[1])
epi=float(line1[2])

x=read1[1].split()
y_str=read1[2].split()
y=[]
for i in range(n):
    temp1=int(y_str[i])
    y.append(temp1)

p=read1[3].split()

v=[]

v.append(float(x[0])-0.5)

for i in range(n-1):
    temp1=(float(x[i])+float(x[i+1]))/2.0
    v.append(temp1)

v.append(float(x[n-1])+0.5)

#print(v)

def errorRate(p1,v1):
    smaller_r_plus=0.0
    smaller_r_minus=0.0
    smaller_w_plus=0.0
    smaller_w_minus=0.0
    smaller_G=0.0
    y_output1=[]
    for i in range(n):
        if (float(x[i])<v1):
            y_output1.append(1)
        else:
            y_output1.append(-1)
    #print(y_output1)
    
    for i in range(n):
        if ((y[i]==1) and (y_output1[i]==1)):
            smaller_r_plus=smaller_r_plus+float(p1[i])
        elif ((y[i]==-1) and (y_output1[i]==-1)):
            smaller_r_minus=smaller_r_minus+float(p1[i])
        elif ((y[i]==1) and (y_output1[i]==-1)):
            smaller_w_plus=smaller_w_plus+float(p1[i])
        elif ((y[i]==-1) and (y_output1[i]==1)):
            smaller_w_minus=smaller_w_minus+float(p1[i])

    temp1=smaller_r_plus*smaller_w_minus
    temp2=math.sqrt(temp1)
    temp3=smaller_w_plus*smaller_r_minus
    temp4=math.sqrt(temp3)
    smaller_G=temp2+temp4
    #print(smaller_G)

    larger_r_plus=0.0
    larger_r_minus=0.0
    larger_w_plus=0.0
    larger_w_minus=0.0
    larger_G=0.0
    y_output2=[]
    for i in range(n):
        if (float(x[i])>v1):
            y_output2.append(1)
        else:
            y_output2.append(-1)
    #print(y_output2)

    for i in range(n):
        if ((y[i]==1) and (y_output2[i]==1)):
            larger_r_plus=larger_r_plus+float(p1[i])
        elif ((y[i]==-1) and (y_output2[i]==-1)):
            larger_r_minus=larger_r_minus+float(p1[i])
        elif ((y[i]==1) and (y_output2[i]==-1)):
            larger_w_plus=larger_w_plus+float(p1[i])
        elif ((y[i]==-1) and (y_output2[i]==1)):
            larger_w_minus=larger_w_minus+float(p1[i])

    temp5=larger_r_plus*larger_w_minus
    temp6=math.sqrt(temp5)
    temp7=larger_w_plus*larger_r_minus
    temp8=math.sqrt(temp7)
    larger_G=temp6+temp8
    #print(larger_G)

            

    PJ=[]
    HTX=[]
    
    if (smaller_G<larger_G):
        flag1="smaller"
        value1=smaller_G
        PJ.append(smaller_r_plus)
        PJ.append(smaller_r_minus)
        PJ.append(smaller_w_plus)
        PJ.append(smaller_w_minus)
        HTX=y_output1[:]
    else:
        flag1="larger"
        value1=larger_G
        PJ.append(larger_r_plus)
        PJ.append(larger_r_minus)
        PJ.append(larger_w_plus)
        PJ.append(larger_w_minus)
        HTX=y_output2[:]

    return {'output1':flag1,'output2':value1,'output3':PJ,'output4':HTX}

def selectH(p1):
    flags='smaller'
    values=100000.0
    index1=0
    PJ1=[]
    HTX1=[]
    for i in range(n+1):
        v_temp=v[i]
        #print(v_temp)
        temp_result=errorRate(p1,v_temp)
        temp_flag1=temp_result['output1']
        temp_value1=temp_result['output2']
        temp_PJ=temp_result['output3']
        temp_HTX=temp_result['output4']
        #print(temp_flag1)
        #print(temp_value1)
        #print(temp_PJ)
        if (temp_value1<values):
            flags=temp_flag1
            index1=i
            values=temp_value1
            PJ1=temp_PJ[:]
            HTX1=temp_HTX[:]

    #print(PJ1)
    #print(HTX1)

    tempp1=(PJ1[0]+epi)/(PJ1[3]+epi)
    C_plus=0.5*math.log(tempp1)

    tempp3=(PJ1[2]+epi)/(PJ1[1]+epi)
    C_minus=0.5*math.log(tempp3)

    #print(C_plus)
    #print(C_minus)

    GT=[]
    
    for i in range(n):
        if (HTX1[i]==1):            
            GT.append(C_plus)
            
        elif (HTX1[i]==-1):            
            GT.append(C_minus)

    #print(GT)
    
    pre_p=[]
    for i in range(n):
        temp1=-y[i]*GT[i]
        temp2=math.exp(temp1)
        temp3=p1[i]*temp2
        pre_p.append(temp3)

    Z1=sum(pre_p)

    new_p=[]
    for i in range(n):
        temp4=pre_p[i]/Z1
        new_p.append(temp4)
    

    return {'output5':flags,'output6':index1,'output7':values,'output8':PJ1,'output9':HTX1,'output10':Z1,'output11':new_p,'output12':C_plus,'output13':C_minus,'output14':GT}

p3=p[:]
p2=[]

for i in range(n):
    temp1=float(p3[i])
    p2.append(temp1)
#print(p2)

accumulated=[]
for i in range(n):
    accumulated.append(0.0)
    
bound=1.0
read_str2=''

for i in range(T):
    print('Round '+str(i+1)+":")       
    results1=selectH(p2)
    out_flags=results1['output5']
    out_index=results1['output6']
    out_values=results1['output7']
    out_PJ=results1['output8']
    out_HTX=results1['output9']
    out_Z=results1['output10']
    p2=results1['output11']
    out_C_plus=results1['output12']
    out_C_minus=results1['output13']
    out_GT=results1['output14']
    

    if (out_flags=='smaller'):
        temp1=v[out_index]
        print('The selected weak classifier: h'+str(i+1)+' is: '+'v<'+str(temp1)+'.')
        read_str='h(x<'+str(temp1)+')'
    else:
        temp1=v[out_index]
        print('The selected weak classifier: h'+str(i+1)+' is: '+'v>'+str(temp1)+'.')
        read_str='h(x>'+str(temp1)+')'

    
    print('The G error value of h'+str(i+1)+' is: '+str(out_values)+'.')

    print('The weights C_plus and C_minus are: '+str(out_C_plus)+' and '+str(out_C_minus)+', respectively.')

    print('The probabilities normalization factor: Z'+str(i+1)+' is: '+str(out_Z)+'.')

    print('The probabilities after normalization: p'+str(i+1)+' is: '+str(p2)+'.')

    for i in range(n):
        accumulated[i]=accumulated[i]+out_GT[i]

    print('The values f for each one of the examples are: '+str(accumulated)+'.')

    sign=[]

    for i in range(n):
        if (accumulated[i]>0.0):
            sign.append(1)
        elif (accumulated[i]<=0.0):
            sign.append(-1)

    error_count=0
    for i in range(n):
        if (sign[i]!=y[i]):
            error_count=error_count+1

    error_rate=error_count/float(n)

    print('The error of the boosted classifier: E'+str(i+1)+' is:'+str(error_rate)+'.')

    bound=bound*out_Z

    print('The bound on E'+str(i+1)+' is: '+str(bound)+'.')

    
    

    

    

    


        
        



















            
            
