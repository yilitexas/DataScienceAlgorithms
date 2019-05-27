function X=maxprod(A,w,its)

%our maxprod function works properly on all tree structures, as tested by
%certain examples listed in maxprod_test.


size1=size(A);
size_w=size(w);
k=size_w(2);
N=size1(1);
M=N*N;

%Step 1: start point: calculate the message matrix using the max-product;
%The matrix C is to record the value of messages, and the matrix C1 is to
%record the maximum assignments for each message.

C=zeros(M,k);
C1=zeros(M,k);

function r1=phi(xi)
r1=exp(w(xi));
end

function r2=psi2(xi,xj)
if (xi==xj)
    r2=0;
else
    r2=1;
end
end


for i=1:N
    for j=1:N
        index0=(i-1)*N+j;
        
        if (A(i,j)==1) 
            
            C(index0,:)=1;
        end
    end
end

flag_v=zeros(M,1);

for i=1:M
    if (C(i,1)==1)
        flag_v(i,1)=1;
    end
end


for iteration=1:its
for i=1:N
    for j=1:N
        index1=(i-1)*N+j;
        
        if (flag_v(index1,1)~=0)
            index1_sum=0;
              
            for l=1:k
                temp_message1=0;
                max_index=0;
                for m=1:k
                    phi_value=phi(m);
                    psi_value=psi2(m,l);
                    temp_message2=phi_value*psi_value;
                    for q=1:N
                        temp1=(q-1)*N+i;
                        temp2=C(temp1,m);
                        if ((temp2~=0) && (q~=j))
                            temp_message2=temp_message2*temp2;
                        end
                    end
                 if (temp_message2>temp_message1)
                     temp_message1=temp_message2;
                     max_index=m;
                 end
                end
            
                C(index1,l)=temp_message1;
                C1(index1,l)=max_index;
                index1_sum=index1_sum+C(index1,l);
            end
        
            for l=1:k
                
                C(index1,l)=C(index1,l)/index1_sum;
                
            end
        
        end
    end
end


end

display(C);
display(C1); %end of Step 1


%Step 2: start point: using the C1 index matrix to find the maximal
%assignment;
%The B1 matrix is the assignment vector for each Xi (each column), for each vertex
%(each row). Please note that for the tree structure, every vertex gives
%the same maximum assignment vectors. That is why every row has the same
%values.

B1=zeros(N,N);

for i=1:N
    message_max1=0;
    index_b=0;
    for j=1:k
        message_total1=phi(j);
        for l=1:N
            index11=(l-1)*N+i;
            if (C(index11,j)~=0)
                message_total1=message_total1*C(index11,j);
            end
        end
        if (message_total1>message_max1)
            message_max1=message_total1;
            index_b=j;
        end
    end
    
    B1(i,i)=index_b;
    
    for its=1:N
    for t1=1:N
        if (B1(i,t1)==0)
            for t2=1:N
                if (t2~=t1) && (B1(i,t2)~=0)
                    index51=(t1-1)*N+t2;
                    index52=B1(i,t2);
                    temp51=C1(index51,index52);
                    if (temp51~=0)
                    B1(i,t1)=temp51;
                    end
                end
            end
        end
    end
    end
        
        
end
        


display(B1); %end of Step 2;



end
                
                    








