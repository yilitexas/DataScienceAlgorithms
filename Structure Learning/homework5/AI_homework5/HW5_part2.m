clc
clear all

M=dlmread('train.txt');

size1=size(M);
num1=size1(1);

p=zeros(19,76);
p(1,1)=0; p(1,2)=1; p(2,1)=1; p(2,2)=2; p(2,3)=3; p(2,4)=4; p(3,1)=1; p(3,2)=2; p(3,3)=3; p(3,4)=4;
p(4,1)=1; p(4,2)=2; p(4,3)=3; p(4,4)=4; p(5,1)=1; p(5,2)=2; p(5,3)=3; p(5,4)=4; p(6,1)=0; p(6,2)=1; p(6,3)=2; p(6,4)=3;
p(7,1)=0; p(7,2)=1; p(8,1)=0; p(8,2)=1; p(9,1)=0; p(9,2)=1; p(10,1)=0; p(10,2)=1; p(11,1)=0; p(11,2)=1;
p(12,1)=1; p(12,2)=2; p(12,3)=3; p(12,4)=4; p(12,5)=5; p(13,1)=1; p(13,2)=2; p(13,3)=3; p(13,4)=4; p(13,5)=5;
p(14,1)=1; p(14,2)=2; p(14,3)=3; p(14,4)=4; p(14,5)=5; p(15,1)=1; p(15,2)=2; p(15,3)=3; p(15,4)=4; p(15,5)=5;
p(16,1)=1; p(16,2)=2; p(16,3)=3; p(16,4)=4; p(16,5)=5; p(17,1)=1; p(17,2)=2; p(17,3)=3; p(17,4)=4; p(17,5)=5;

for i=1:76
    p(18,i)=(i-1);
end

for i=1:20
    p(19,i)=(i-1);
end

%for each of the 19 variables, count the occurences for each of its values;
single1=zeros(1,1444);

for i=1:19
    for j=1:76
        temp1=(i-1)*76+j;
        for k=1:num1
            temp2=M(k,i);
            
            if (temp2==(j-1))
                single1(1,temp1)=single1(1,temp1)+1;
            end
        end
    end
end

%single1

%for each pair of the 19 variables, count the concurrent occurences for each of their values;
double1=zeros(1444,1444);

for i1=1:19
    for j1=1:76
        for i2=1:19
            for j2=1:76
                temp1=(i1-1)*76+j1;
                temp2=(i2-1)*76+j2;
                for k1=1:num1
                    temp21=M(k1,i1);
                    temp22=M(k1,i2);
                    
                    if ((temp21==(j1-1)) && (temp22==(j2-1)))
                        double1(temp1,temp2)=double1(temp1,temp2)+1;
                    end
                end
            end
        end
    end
end

%double1

%calculate the empirical mutual information
                    
MI1=zeros(19,19);

for i3=1:19
    for j3=1:19
        temp0=0;
        for i4=1:76
            for j4=1:76
                temp1=(i3-1)*76+i4;
                temp2=(j3-1)*76+j4;
                temp3=double1(temp1,temp2);
                temp4=single1(1,temp1);
                temp5=single1(1,temp2);
                if (((temp4*temp5)~=0) && (temp3~=0))
                    temp6=log(temp3/(temp4*temp5));
                    temp7=temp3*temp6;
                    temp0=temp0+temp7;
                end
            end
        end
        MI1(i3,j3)=temp0;
    end
end

%MI1

%construct the chow-liu tree

S=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, ...
    2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, ...
    3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3, ...
    4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, ...
    5,5,5,5,5,5,5,5,5,5,5,5,5,5, ...
    6,6,6,6,6,6,6,6,6,6,6,6,6, ...
    7,7,7,7,7,7,7,7,7,7,7,7, ...
    8,8,8,8,8,8,8,8,8,8,8, ...
    9,9,9,9,9,9,9,9,9,9, ...
    10,10,10,10,10,10,10,10,10, ...
    11,11,11,11,11,11,11,11, ...
    12,12,12,12,12,12,12, ...
    13,13,13,13,13,13, ...
    14,14,14,14,14, ...
    15,15,15,15, ...
    16,16,16, ...
    17,17, ...
    18];

T=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    6,7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    7,8,9,10,11,12,13,14,15,16,17,18,19, ...
    8,9,10,11,12,13,14,15,16,17,18,19, ...
    9,10,11,12,13,14,15,16,17,18,19, ...
    10,11,12,13,14,15,16,17,18,19, ...
    11,12,13,14,15,16,17,18,19, ...
    12,13,14,15,16,17,18,19, ....
    13,14,15,16,17,18,19, ...
    14,15,16,17,18,19, ...
    15,16,17,18,19, ...
    16,17,18,19, ...
    17,18,19, ...
    18,19, ...
    19];

Q=zeros(1,171);

for i=1:171
    temp1=S(1,i);
    temp2=T(1,i);
    temp3=MI1(temp1,temp2);
    Q(1,i)=-1*temp3;
end

%Q

G1 = graph(S,T,Q);
%p1 = plot(G1,'EdgeLabel',G1.Edges.Weight);
[T1,pred1] = minspantree(G1);
%highlight(p1,T1)
T1.Edges
%T1.Nodes

%determine the marginal counts (6,19), (9,19) and (18,19)

M6_19=zeros(76,76);

for i=1:76
    for j=1:76
        temp1=(6-1)*76+i;
        temp2=(19-1)*76+j;
        temp3=double1(temp1,temp2);
        M6_19(i,j)=temp3;
    end
end

M9_19=zeros(76,76);

for i=1:76
    for j=1:76
        temp1=(9-1)*76+i;
        temp2=(19-1)*76+j;
        temp3=double1(temp1,temp2);
        M9_19(i,j)=temp3;
    end
end

M18_19=zeros(76,76);

for i=1:76
    for j=1:76
        temp1=(18-1)*76+i;
        temp2=(19-1)*76+j;
        temp3=double1(temp1,temp2);
        M18_19(i,j)=temp3;
    end
end

M19=zeros(1,76);

for i=1:76
    temp1=(19-1)*76+i;
    temp2=single1(1,temp1);
    M19(1,i)=temp2;
end

%M6_19

%M9_19

%M18_19

%M19

     
N=dlmread('test.txt');

size2=size(N);
num2=size2(1);

%predict the grades for the test sample

result1=zeros(1,num2);


for i=1:num2
    temp1=N(i,6);
    temp2=N(i,9);
    temp3=N(i,18);
    max2=0.0;
    index2=0;
    
    for j=1:21
        temp4=M6_19((temp1+1),j);
        temp5=M9_19((temp2+1),j);
        temp6=M18_19((temp3+1),j);
        temp7=M19(1,j);
        
        if (temp7~=0)
            temp8=(temp4*temp5*temp6)/(temp7*temp7);
            if (temp8>max2)
                max2=temp8;
                index2=(j-1);
            end
        end
    end
    result1(1,i)=index2;
end

result2=zeros(1,num2);

for i=1:num2
    temp1=N(i,19);
    result2(1,i)=temp1;
end

%calculate the accuracy

count2=0;

for i=1:num2
    if (result1(1,i)==result2(1,i))
        count2=count2+1;
    end
end

accuracy2=count2/num2;

accuracy2
    
    
        
        
        
    



















