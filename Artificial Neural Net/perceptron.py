import math

e0=[0,0,1]
e1=[0,1,1]
e2=[1,0,1]
e3=[1,1,1]

y=[0,1,1,0]

b=1
epi=0.5
omega=[0,0,0]

def h(arrayOmega,arrayE):
    temp0=arrayOmega[0]*float(arrayE[0])
    temp1=arrayOmega[1]*float(arrayE[1])
    temp2=arrayOmega[2]*float(arrayE[2])

    temp=temp0+temp1+temp2
    return temp

def O(h):
    temp=1.0/(1+math.exp(-2*h))
    return temp

def delta(O,y):
    temp=float(O)*(1-O)*(y-O)
    return temp

def epoch(array0):
    #print(array0)
    h0=h(array0,e0)
    O0=O(h0)
    delta0=delta(O0,y[0])
    array1=[]
    temp1=array0[0]+epi*delta0*e0[0]
    array1.append(temp1)
    temp2=array0[1]+epi*delta0*e0[1]
    array1.append(temp2)
    temp3=array0[2]+epi*delta0*e0[2]
    array1.append(temp3)
    #print(array1)

    h1=h(array1,e1)
    O1=O(h1)
    delta1=delta(O1,y[1])
    array2=[]
    temp4=array1[0]+epi*delta1*e1[0]
    array2.append(temp4)
    temp5=array1[1]+epi*delta1*e1[1]
    array2.append(temp5)
    temp6=array1[2]+epi*delta1*e1[2]
    array2.append(temp6)
    #print(array2)

    h2=h(array2,e2)
    O2=O(h2)
    delta2=delta(O2,y[2])
    array3=[]
    temp7=array2[0]+epi*delta2*e2[0]
    array3.append(temp7)
    temp8=array2[1]+epi*delta2*e2[1]
    array3.append(temp8)
    temp9=array2[2]+epi*delta2*e2[2]
    array3.append(temp9)
    #print(array3)

    h3=h(array3,e3)
    O3=O(h3)
    delta3=delta(O3,y[3])
    array4=[]
    temp10=array3[0]+epi*delta3*e3[0]
    array4.append(temp10)
    temp11=array3[1]+epi*delta3*e3[1]
    array4.append(temp11)
    temp12=array3[2]+epi*delta3*e3[2]
    array4.append(temp12)
    #print(array4)

    return array4


N=int(input("times to repeat the epoches are:\n"))

omega1=[0,0,0]

def calEpoch(k):
    if (k==0):
        return omega1
    else:
        return epoch(calEpoch(k-1))

print(calEpoch(N))


        
