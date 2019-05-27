function B=sumprod_HW4(A,w,its)

size1=size(A);
size_w=size(w);
k=size_w(2);
N=size1(1);
M=N*N;

%Step 1 (start point): calculate the message matrix, which is N2*k dimension
C=zeros(M,k);

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
                 temp_message1=temp_message1+temp_message2;
                end
            
                C(index1,l)=temp_message1;
                index1_sum=index1_sum+C(index1,l);
            end
        
            for l=1:k
                
                C(index1,l)=C(index1,l)/index1_sum;
                
            end
        
        end
    end
end

end

%display(C); % end of Step 1: calculating the message matrix;


%Step 2: start point: calculating the singleton and pairwise matrices;
B=zeros(N,k);

for i=1:N
    message_total1_sum=0;
    for j=1:k
        message_total1=phi(j);
        for l=1:N
            index11=(l-1)*N+i;
            if (C(index11,j)~=0)
                message_total1=message_total1*C(index11,j);
            end
        end
        B(i,j)=message_total1;
        message_total1_sum=message_total1_sum+B(i,j);
    end
    
        
    for j=1:k
        B(i,j)=B(i,j)/message_total1_sum;
    end
end



end
                
                    








