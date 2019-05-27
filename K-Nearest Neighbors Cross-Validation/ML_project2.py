import numpy as np
import math

input1=open("test4-1.txt","r")
readin1=input1.readlines()
input1.close()

line1=readin1[0].split()
f=int(line1[0])
m=int(line1[1])
t=int(line1[2])

#print(f)
#print(m)
#print(t)
#print(readin1)

input2=open("test4-2.txt","r")
readin2=input2.readlines()
input2.close()

dimensions=readin2[0].split()
r_num=int(dimensions[0])
c_num=int(dimensions[1])

data1=[]

for i in range(r_num):
    temp1=readin2[i+1].split()
    for j in range(c_num):
        temp2=temp1[j]
        data1.append(temp2)

#print(data1)

index1=-1
ind1=[]
x1=[]
x2=[]
y=[]

index2=-1
u_ind1=[]
u_row1=[]
u_column1=[]

num1=int(r_num*c_num)
#print(num1)
for i in range(num1):
    if (data1[i]!='.'):
        index1=index1+1
        ind1.append(index1)
        temp1=int(i/c_num)
        temp2=i-temp1*c_num
        x1.append(temp2)
        x2.append(temp1)
        y.append(data1[i])

    else:
        index2=index2+1
        u_ind1.append(index2)
        temp1=int(i/c_num)
        temp2=i-temp1*c_num
        u_column1.append(temp2)
        u_row1.append(temp1)

#print(ind1)
#print(x1)
#print(x2)
#print(y)

ori_ind1=ind1[:]
ori_x1=x1[:]
ori_x2=x2[:]
ori_y=y[:]

#print(u_ind1)
#print(u_row1)
#print(u_column1)

len4=len(u_ind1)

def shuffle(seq):
    temp_ind1=[]
    temp_x1=[]
    temp_x2=[]
    temp_y=[]
    for i in range(m):
        temp1=int(seq[i])
        temp_ind1.append(ind1[temp1])
        temp_x1.append(x1[temp1])
        temp_x2.append(x2[temp1])
        temp_y.append(y[temp1])

    return {'output1':temp_ind1,'output2':temp_x1,'output3':temp_x2,'output4':temp_y}     

def NN(t_ind1,t_x1,t_x2,t_y,i_ind1,i_x1,i_x2,k_nei):
    flag1='-'
    len2=len(t_ind1)
    dis1=[]
    for i in range(len2):
        temp1=(t_x1[i]-i_x1)*(t_x1[i]-i_x1)
        temp2=(t_x2[i]-i_x2)*(t_x2[i]-i_x2)
        temp3=temp1+temp2
        dis1.append(temp3)

	#print("t_x1[i] is: "+str(t_x1[i]))
	#print("t_x2[i] is: "+str(t_x2[i]))
	#print("t_y[i] is: "+str(t_y[i]))
	#print("i_x1 is: "+str(i_x1))
	#print("i_x2 is: "+str(i_x2))

    #print(dis1)
    for i in range(len2):
        for j in range(i,len2):
            if (dis1[i]>dis1[j]):
                temp4=t_ind1[i]
                t_ind1[i]=t_ind1[j]
                t_ind1[j]=temp4
                temp5=t_x1[i]
                t_x1[i]=t_x1[j]
                t_x1[j]=temp5
                temp6=t_x2[i]
                t_x2[i]=t_x2[j]
                t_x2[j]=temp6
                temp7=t_y[i]
                t_y[i]=t_y[j]
                t_y[j]=temp7
                temp8=dis1[i]
                dis1[i]=dis1[j]
                dis1[j]=temp8
    
    #print(dis1)
    #print(t_ind1)
    #print(t_x1)
    #print(t_x2)
    #print(t_y)
    if (k_nei>=len2):
        p1=0
        n1=0
        for i in range(len2):
            if (t_y[i]=='+'):
                p1=p1+1
            else:
                n1=n1+1
        if (p1>n1):
            flag1='+'
        else:
            flag1='-'
    else:
        min1=dis1[k_nei-1]
	#print(min1)
        count1=0
	#print(count1)
        for i in range(len2):
            if (dis1[i]<=min1):
                count1=count1+1

        p1=0
        n1=0
        for i in range(count1):
            if(t_y[i]=='+'):
                p1=p1+1
            else:
                n1=n1+1

	#print(p1)
	#print(n1)
        if (p1>n1):
            flag1='+'
        else:
            flag1='-'
	#print("flag1 is: "+str(flag1))

    return flag1


len1=int(m/f)

def divided(ind1,x1,x2,y,d,knei):
    test_ind1=[]
    test_x1=[]
    test_x2=[]
    test_y=[]
    train_ind1=[]
    train_x1=[]
    train_x2=[]
    train_y=[]
    if (d<(f-1)):
        for k in range(m):
            if ((k>=d*len1) and (k<(d+1)*len1)):
                test_ind1.append(ind1[k])
                test_x1.append(x1[k])
                test_x2.append(x2[k])
                test_y.append(y[k])
            else:
                train_ind1.append(ind1[k])
                train_x1.append(x1[k])
                train_x2.append(x2[k])
                train_y.append(y[k])

    else:
        for k in range(m):
            if (k>=(f-1)*len1):
                test_ind1.append(ind1[k])
                test_x1.append(x1[k])
                test_x2.append(x2[k])
                test_y.append(y[k])
            else:
                train_ind1.append(ind1[k])
                train_x1.append(x1[k])
                train_x2.append(x2[k])
                train_y.append(y[k])

    #print(test_ind1)
    #print(test_x1)
    #print(test_x2)
    #print(test_y)
    #print(train_ind1)
    #print(train_x1)
    #print(train_x2)
    #print(train_y)
    
    len9=len(test_ind1)
    error_count1=0
    for i in range(len9):
        i_ind1_tested=test_ind1[i]
        i_x1_tested=test_x1[i]
        i_x2_tested=test_x2[i]
        i_y_tested=test_y[i]

        result1=NN(train_ind1,train_x1,train_x2,train_y,i_ind1_tested,i_x1_tested,i_x2_tested,knei)
        #print("result1 is : "+str(result1))
        #print("i_y_tested is "+str(i_y_tested))
            
        if (result1!=i_y_tested):
            error_count1=error_count1+1

    return error_count1

total_e=[]
total_sigma=[]

for knei in range(5):
    knei1=knei+1
    err=[]
    for i in range(t):
        temp_seq=readin1[i+1].split()
        #print(i)
        #print(temp_seq)
        temp_result=shuffle(temp_seq)
        ind1_shuffled=temp_result['output1']
        x1_shuffled=temp_result['output2']
        x2_shuffled=temp_result['output3']
        y_shuffled=temp_result['output4']
        #print(ind1_shuffled)
        #print(x1_shuffled)
        #print(x2_shuffled)
        #print(y_shuffled)
        total_error_count1=0
        for j in range(f):
            temp1=divided(ind1_shuffled,x1_shuffled,x2_shuffled,y_shuffled,j,knei1)
            #print("one fold error count is: "+str(temp1))
            total_error_count1=total_error_count1+temp1

        rate1=total_error_count1/float(m)
        err.append(rate1)

    #print(err)

    sum1=0
    for i in range(t):
        sum1=sum1+err[i]
    e=sum1/float(t)

    std1=0.0
    for i in range(t):
        temp1=(err[i]-e)*(err[i]-e)
        std1=std1+temp1

    if (t==1):
	STD2="NaN"
    else:
	STD1=std1/(t-1)
    	STD2=math.sqrt(STD1)

    total_e.append(e)
    total_sigma.append(STD2)

    print("for "+str(knei1)+"-nearest neighbor, the e is: "+str(e))
    print("for "+str(knei1)+"-nearest neighbor, the sigma is: "+str(STD2))
            
            
for knei in range(5):
    knei1=knei+1
    flag_result1=[]

    #print(ori_ind1)
    #print(ori_x1)
    #print(ori_x2)
    #print(ori_y)
    #print(u_row1)
    #print(u_column1)
    #print(flag_result1)

    for i in range(len4):
        copy_ori_ind1=ori_ind1[:]
        copy_ori_x1=ori_x1[:]
        copy_ori_x2=ori_x2[:]
        copy_ori_y=ori_y[:]
        #print(ori_ind1)
        result2=NN(copy_ori_ind1,copy_ori_x1,copy_ori_x2,copy_ori_y,u_ind1[i],u_column1[i],u_row1[i],knei1)
        #print(ori_ind1)
        flag_result1.append(result2)

    
    print(" k="+str(knei1)+" e="+str(total_e[knei])+" sigma="+str(total_sigma[knei]))
    m_output=np.empty([r_num,c_num],dtype=str)

    #print(ori_ind1)
    #print(ori_x1)
    #print(ori_x2)
    #print(ori_y)
    #print(u_row1)
    #print(u_column1)
    #print(flag_result1)

    for i in range(r_num):
        for j in range(c_num):
            for k in range(m):
                if ((i==ori_x2[k]) and (j==ori_x1[k])):
                    m_output[i][j]=str(ori_y[k])

            for l in range(len4):
                temp_flag1=flag_result1[l]
		#print(temp_flag1)
                if ((i==u_row1[l]) and (j==u_column1[l])):
                    m_output[i][j]=str(temp_flag1)

    #print(m_output)

    for i in range(r_num):
	temp_str1=""
        for j in range(c_num):
            temp9=m_output[i][j]
            temp_str1=temp_str1+temp9+" "
        temp_str1=temp_str1+"\n"
	print(temp_str1)