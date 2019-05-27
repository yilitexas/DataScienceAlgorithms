import math

input1=open("file2.txt","r")
read1=input1.readlines()
#print(read1)

line1=read1[0].split()
T=int(line1[0])
n=int(line1[1])

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
    smaller=0.0
    y_output1=[]
    for i in range(n):
        if (float(x[i])<v1):
            y_output1.append(1)
        else:
            y_output1.append(-1)
    #print(y_output1)
    
    for i in range(n):
        if (y_output1[i]!=y[i]):
            smaller=smaller+float(p1[i])
    #print(smaller)

    larger=0.0
    y_output2=[]
    for i in range(n):
        if (float(x[i])>v1):
            y_output2.append(1)
        else:
            y_output2.append(-1)
    #print(y_output2)

    for i in range(n):
        if (y_output2[i]!=y[i]):
            larger=larger+float(p1[i])
    #print(larger)
            

    y_output3=[]
    
    if (smaller<larger):
        flag1="smaller"
        value1=smaller
        y_output3=y_output1[:]
    else:
        flag1="larger"
        value1=larger
        y_output3=y_output2[:]

    return {'output1':flag1,'output2':value1,'output3':y_output3}

def selectH(p1):
    flags='smaller'
    values=100000.0
    index1=0
    y_read1=[]
    for i in range(n+1):
        v_temp=v[i]
        #print(v_temp)
        temp_result=errorRate(p1,v_temp)
        temp_flag1=temp_result['output1']
        temp_value1=temp_result['output2']
        temp_y_output=temp_result['output3']
        #print(temp_flag1)
        #print(temp_value1)
        #print(temp_y_output)
        if (temp_value1<values):
            flags=temp_flag1
            index1=i
            values=temp_value1
            y_read1=temp_y_output[:]

    return {'output4':flags,'output5':index1,'output6':values,'output7':y_read1}

def at(error1):
    temp1=(1-error1)/error1
    temp2=0.5*math.log(temp1)

    return temp2

def qi(y1,error1):
    q=[]
    for i in range(n):
        temp1=y1[i]
        temp2=y[i]
        if (temp1==temp2):
            temp3=math.exp(-error1)

        else:
            temp3=math.exp(error1)

        q.append(temp3)

    return q

def piqi(pi,qi):
    pq=[]
    for i in range(n):
        temp1=pi[i]*qi[i]
        pq.append(temp1)

    return pq

def normalizedpi(pq1):
    temp1=sum(pq1)
    normalized_p=[]
    for i in range(n):
        temp2=pq1[i]/temp1
        normalized_p.append(temp2)

    return normalized_p

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
    out_index=results1['output5']
    out_flags=results1['output4']

    if (out_flags=='smaller'):
        temp1=v[out_index]
        print('The selected weak classifier: h'+str(i+1)+' is: '+'v<'+str(temp1)+'.')
        read_str='h(x<'+str(temp1)+')'
    else:
        temp1=v[out_index]
        print('The selected weak classifier: h'+str(i+1)+' is: '+'v>'+str(temp1)+'.')
        read_str='h(x>'+str(temp1)+')'

    out_values=results1['output6']
    print('The error of h'+str(i+1)+' e is: '+str(out_values)+'.')

    out_y_output=results1['output7']

    a=at(out_values)
    print('The weight of h'+str(i+1)+' a is: '+str(a)+'.')
    read_str1=str(a)+'*'+read_str+'+'
    read_str2=read_str2+read_str1
    len1=len(read_str2)
    read_str3=read_str2[:(len1-1)]

    out_q=[]
    out_q=qi(out_y_output,a)

    out_pq=[]
    out_pq=piqi(p2,out_q)

    Z=sum(out_pq)
    print('The probabilities normalization factor: Z'+str(i+1)+' is: '+str(Z)+'.')

    p2=normalizedpi(out_pq)
    print('The probabilities after normalization: p'+str(i+1)+' is: '+str(p2)+'.')

    print('The boosted classifier f'+str(i+1)+' is: '+read_str3+'.')

    accumulated_read=[]
    
    for j in range(n):
        temp4=out_y_output[j]*a
        accumulated[j]=accumulated[j]+temp4
        if (accumulated[j]<0):
            accumulated_read.append(-1)
        else:
            accumulated_read.append(1)

    total_error=0
    for k in range(n):
        if (accumulated_read[k]!=y[k]):
            total_error=total_error+1

    error_rate=total_error/float(n)

    print('The error of the boosted classifier: E'+str(i+1)+' is: '+str(error_rate)+'.')

    bound=bound*Z

    print('The bound on E'+str(i+1)+' is: '+str(bound)+'.')

    
    

    

    

    


        
        



















            
            
