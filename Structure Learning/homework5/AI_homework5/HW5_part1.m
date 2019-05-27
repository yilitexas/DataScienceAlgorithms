clc
clear all

M=dlmread('train.txt');

size1=size(M);
num1=size1(1);

N=dlmread('test.txt');

size2=size(N);
num2=size2(1);

P19=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

%calculate the class prior probabilities
prior1=zeros(1,21);

for i=1:num1
    for k=1:21
        if (M(i,19)==(k-1))
            prior1(1,k)=prior1(1,k)+1;
        end
    end
end

sum0=sum(prior1);
prior1=prior1/sum0;
%prior1     

%calculate the likelihood
count1=zeros(138,21);

for i=1:num1
    for j=1:21
        if ((M(i,1)==0) && (M(i,19)==P19(j)))
            count1(1,j)=count1(1,j)+1;
        elseif ((M(i,1)==1) && (M(i,19)==P19(j)))
            count1(2,j)=count1(2,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,2)==1) && (M(i,19)==P19(j)))
            count1(3,j)=count1(3,j)+1;
        elseif ((M(i,2)==2) && (M(i,19)==P19(j)))
            count1(4,j)=count1(4,j)+1;
        elseif ((M(i,2)==3) && (M(i,19)==P19(j)))
            count1(5,j)=count1(5,j)+1;
        elseif ((M(i,2)==4) && (M(i,19)==P19(j)))
            count1(6,j)=count1(6,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,3)==1) && (M(i,19)==P19(j)))
            count1(7,j)=count1(7,j)+1;
        elseif ((M(i,3)==2) && (M(i,19)==P19(j)))
            count1(8,j)=count1(8,j)+1;
        elseif ((M(i,3)==3) && (M(i,19)==P19(j)))
            count1(9,j)=count1(9,j)+1;
        elseif ((M(i,3)==4) && (M(i,19)==P19(j)))
            count1(10,j)=count1(10,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,4)==1) && (M(i,19)==P19(j)))
            count1(11,j)=count1(11,j)+1;
        elseif ((M(i,4)==2) && (M(i,19)==P19(j)))
            count1(12,j)=count1(12,j)+1;
        elseif ((M(i,4)==3) && (M(i,19)==P19(j)))
            count1(13,j)=count1(13,j)+1;
        elseif ((M(i,4)==4) && (M(i,19)==P19(j)))
            count1(14,j)=count1(14,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,5)==1) && (M(i,19)==P19(j)))
            count1(15,j)=count1(15,j)+1;
        elseif ((M(i,5)==2) && (M(i,19)==P19(j)))
            count1(16,j)=count1(16,j)+1;
        elseif ((M(i,5)==3) && (M(i,19)==P19(j)))
            count1(17,j)=count1(17,j)+1;
        elseif ((M(i,5)==4) && (M(i,19)==P19(j)))
            count1(18,j)=count1(18,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,6)==0) && (M(i,19)==P19(j)))
            count1(19,j)=count1(19,j)+1;
        elseif ((M(i,6)==1) && (M(i,19)==P19(j)))
            count1(20,j)=count1(20,j)+1;
        elseif ((M(i,6)==2) && (M(i,19)==P19(j)))
            count1(21,j)=count1(21,j)+1;
        elseif ((M(i,6)==3) && (M(i,19)==P19(j)))
            count1(22,j)=count1(22,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,7)==0) && (M(i,19)==P19(j)))
            count1(23,j)=count1(23,j)+1;
        elseif ((M(i,7)==1) && (M(i,19)==P19(j)))
            count1(24,j)=count1(24,j)+1;
        
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,8)==0) && (M(i,19)==P19(j)))
            count1(25,j)=count1(25,j)+1;
        elseif ((M(i,8)==1) && (M(i,19)==P19(j)))
            count1(26,j)=count1(26,j)+1;
        
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,9)==0) && (M(i,19)==P19(j)))
            count1(27,j)=count1(27,j)+1;
        elseif ((M(i,9)==1) && (M(i,19)==P19(j)))
            count1(28,j)=count1(28,j)+1;
        
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,10)==0) && (M(i,19)==P19(j)))
            count1(29,j)=count1(29,j)+1;
        elseif ((M(i,10)==1) && (M(i,19)==P19(j)))
            count1(30,j)=count1(30,j)+1;
        
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,11)==0) && (M(i,19)==P19(j)))
            count1(31,j)=count1(31,j)+1;
        elseif ((M(i,11)==1) && (M(i,19)==P19(j)))
            count1(32,j)=count1(32,j)+1;
        
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,12)==1) && (M(i,19)==P19(j)))
            count1(33,j)=count1(33,j)+1;
        elseif ((M(i,12)==2) && (M(i,19)==P19(j)))
            count1(34,j)=count1(34,j)+1;
        elseif ((M(i,12)==3) && (M(i,19)==P19(j)))
            count1(35,j)=count1(35,j)+1;
        elseif ((M(i,12)==4) && (M(i,19)==P19(j)))
            count1(36,j)=count1(36,j)+1;
        elseif ((M(i,12)==5) && (M(i,19)==P19(j)))
            count1(37,j)=count1(37,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,13)==1) && (M(i,19)==P19(j)))
            count1(38,j)=count1(38,j)+1;
        elseif ((M(i,13)==2) && (M(i,19)==P19(j)))
            count1(39,j)=count1(39,j)+1;
        elseif ((M(i,13)==3) && (M(i,19)==P19(j)))
            count1(40,j)=count1(40,j)+1;
        elseif ((M(i,13)==4) && (M(i,19)==P19(j)))
            count1(41,j)=count1(41,j)+1;
        elseif ((M(i,13)==5) && (M(i,19)==P19(j)))
            count1(42,j)=count1(42,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,14)==1) && (M(i,19)==P19(j)))
            count1(43,j)=count1(43,j)+1;
        elseif ((M(i,14)==2) && (M(i,19)==P19(j)))
            count1(44,j)=count1(44,j)+1;
        elseif ((M(i,14)==3) && (M(i,19)==P19(j)))
            count1(45,j)=count1(45,j)+1;
        elseif ((M(i,14)==4) && (M(i,19)==P19(j)))
            count1(46,j)=count1(46,j)+1;
        elseif ((M(i,14)==5) && (M(i,19)==P19(j)))
            count1(47,j)=count1(47,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,15)==1) && (M(i,19)==P19(j)))
            count1(48,j)=count1(48,j)+1;
        elseif ((M(i,15)==2) && (M(i,19)==P19(j)))
            count1(49,j)=count1(49,j)+1;
        elseif ((M(i,15)==3) && (M(i,19)==P19(j)))
            count1(50,j)=count1(50,j)+1;
        elseif ((M(i,15)==4) && (M(i,19)==P19(j)))
            count1(51,j)=count1(51,j)+1;
        elseif ((M(i,15)==5) && (M(i,19)==P19(j)))
            count1(52,j)=count1(52,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,16)==1) && (M(i,19)==P19(j)))
            count1(53,j)=count1(53,j)+1;
        elseif ((M(i,16)==2) && (M(i,19)==P19(j)))
            count1(54,j)=count1(54,j)+1;
        elseif ((M(i,16)==3) && (M(i,19)==P19(j)))
            count1(55,j)=count1(55,j)+1;
        elseif ((M(i,16)==4) && (M(i,19)==P19(j)))
            count1(56,j)=count1(56,j)+1;
        elseif ((M(i,16)==5) && (M(i,19)==P19(j)))
            count1(57,j)=count1(57,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        if ((M(i,17)==1) && (M(i,19)==P19(j)))
            count1(58,j)=count1(58,j)+1;
        elseif ((M(i,17)==2) && (M(i,19)==P19(j)))
            count1(59,j)=count1(59,j)+1;
        elseif ((M(i,17)==3) && (M(i,19)==P19(j)))
            count1(60,j)=count1(60,j)+1;
        elseif ((M(i,17)==4) && (M(i,19)==P19(j)))
            count1(61,j)=count1(61,j)+1;
        elseif ((M(i,17)==5) && (M(i,19)==P19(j)))
            count1(62,j)=count1(62,j)+1;
        end
    end
end

for i=1:num1
    for j=1:21
        for k=1:76
            if ((M(i,18)==(k-1)) && (M(i,19)==P19(j)))
                count1((62+k),j)=count1((62+k),j)+1;
            end
        end
    end
end        


for i=1:21
    sum1=0;
    for j=1:2
        sum1=sum1+count1(j,i);
    end
    for j=1:2
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=3:6
        sum1=sum1+count1(j,i);
    end
    for j=3:6
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=7:10
        sum1=sum1+count1(j,i);
    end
    for j=7:10
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=11:14
        sum1=sum1+count1(j,i);
    end
    for j=11:14
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=15:18
        sum1=sum1+count1(j,i);
    end
    for j=15:18
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=19:22
        sum1=sum1+count1(j,i);
    end
    for j=19:22
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=23:24
        sum1=sum1+count1(j,i);
    end
    for j=23:24
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=25:26
        sum1=sum1+count1(j,i);
    end
    for j=25:26
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=27:28
        sum1=sum1+count1(j,i);
    end
    for j=27:28
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=29:30
        sum1=sum1+count1(j,i);
    end
    for j=29:30
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=31:32
        sum1=sum1+count1(j,i);
    end
    for j=31:32
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=33:37
        sum1=sum1+count1(j,i);
    end
    for j=33:37
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=38:42
        sum1=sum1+count1(j,i);
    end
    for j=38:42
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=43:47
        sum1=sum1+count1(j,i);
    end
    for j=43:47
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=48:52
        sum1=sum1+count1(j,i);
    end
    for j=48:52
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=53:57
        sum1=sum1+count1(j,i);
    end
    for j=53:57
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=58:62
        sum1=sum1+count1(j,i);
    end
    for j=58:62
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

for i=1:21
    sum1=0;
    for j=63:138
        sum1=sum1+count1(j,i);
    end
    for j=63:138
        if (sum1~=0)
            count1(j,i)=count1(j,i)/sum1;
        end
    end
end

%display(count1);

%determine the maximal posterior probabilities
sample1=zeros(1,num2);

for i=1:num2
    max1=0.0;
    temp32=0;
    for index=1:21
        temp61=N(i,1)+1;
        temp11=count1(temp61,index);
        temp62=N(i,2)+2;
        temp12=count1(temp62,index);
        temp63=N(i,3)+6;
        temp13=count1(temp63,index);
        temp64=N(i,4)+10;
        temp14=count1(temp64,index);
        temp65=N(i,5)+14;
        temp15=count1(temp65,index);
        temp66=N(i,6)+19;
        temp16=count1(temp66,index);
        temp67=N(i,7)+23;
        temp17=count1(temp67,index);
        temp68=N(i,8)+25;
        temp18=count1(temp68,index);
        temp69=N(i,9)+27;
        temp19=count1(temp69,index);
        temp70=N(i,10)+29;
        temp20=count1(temp70,index);
        temp71=N(i,11)+31;
        temp21=count1(temp71,index);
        temp72=N(i,12)+32;
        temp22=count1(temp72,index);
        temp73=N(i,13)+37;
        temp23=count1(temp73,index);
        temp74=N(i,14)+42;
        temp24=count1(temp74,index);
        temp75=N(i,15)+47;
        temp25=count1(temp75,index);
        temp76=N(i,16)+52;
        temp26=count1(temp76,index);
        temp77=N(i,17)+57;
        temp27=count1(temp77,index);
        temp78=N(i,18)+63;
        temp28=count1(temp78,index);
        temp29=prior1(1,index);

        prob1=temp11*temp12*temp13*temp14*temp15*temp16*temp17*temp18*temp19*temp20*temp21*temp22*temp23*temp24*temp25*temp26*temp27*temp28*temp29;
        %display(prob1)
        if (prob1>=max1)
            max1=prob1;
            temp32=(index-1);
        end
        
    end
    
    sample1(1,i)=temp32;
    %display(max1);
    %display(temp32);
end

sample1

sample2=zeros(1,num2);

for i=1:num2
    sample2(1,i)=N(i,19);
end

sample2

%calculate the accruacy for the Naive Bayes calssification
count11=0;
for i=1:num2
    if (sample1(1,i)==sample2(1,i))
        count11=count11+1;
    end
end

accuracy=count11/num2;

accuracy


