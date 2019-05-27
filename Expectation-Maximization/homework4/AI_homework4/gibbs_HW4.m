function samples=gibbs_HW4(A,w,burnin,its)

size1=size(A);
size_w=size(w);
k=size_w(2);
N=size1(1);

%display(k);
%display(N);

M=1+burnin+its;
C=zeros(M,N);

%%we try to generate an initial assignment with non-zero joint probability;
round=ceil(N/k);

for i=1:(round+1)
    for j=1:k
        index1=(i-1)*k+j;
        if (index1<=N)
            C(1,index1)=j;
        end
    end
end

%display(C);
%calculate the singleton potential function

function r1=phi(xi)
    r1=exp(w(xi));
end

%calculate the pairwise potential function

function r2=psi2(xi,xj)
    if (xi==xj)
        r2=0;
    else
        r2=1;
    end
end

%this function is to take a specific x assignment, then calculate its joint
%probability;

function marg=marginal(x)
    total1=1;
    for i1=1:N
        temp1=x(i1,1);
        temp2=phi(temp1);
        total1=total1*temp2;
    end
    
    for i2=1:(N-1)
        for j1=(i2+1):N
            if (A(i2,j1)~=0)
                temp1=x(i2,1);
                temp2=x(j1,1);
                temp3=psi2(temp1,temp2);
                total1=total1*temp3;
            end
        end
    end
    
    marg=total1;
end

        
%Here we perform the Gibbs sampling and then generate new samples for
%burnin+its times;
for i=2:M
    for j=1:N
        conditional=zeros(k,1);
        for q=1:k
                    
            vec1=zeros(N,1);
            for l=1:(j-1)
                vec1(l,1)=C(i,l);
            end
            
            vec1(j,1)=q;
            
            for m=(j+1):N
                vec1(m,1)=C((i-1),m);
            end
                    
            numerator1=marginal(vec1);
                   
            denominator1=0;
            
            for p=1:k
                
                vec1(j,1)=p;
                temp_marg=marginal(vec1);
                denominator1=denominator1+temp_marg;
            end
                    
            conditional_p=numerator1/denominator1;
            
            conditional(q,1)=conditional_p;
            
        end
        
        sum1=sum(conditional);
        for s=1:k
            conditional(s,1)=conditional(s,1)/sum1;
        end
        
        %display(conditional);       
                
        cdf1=zeros(k,1);
        aggregate1=0;
        for s1=1:k
            aggregate1=aggregate1+conditional(s1,1);
            cdf1(s1,1)=aggregate1;
        end
            
        indicator1=rand;
                
        if (indicator1<cdf1(1,1))
            C(i,j)=1;
        else
            for t=1:(k-1)            
                if (indicator1>=cdf1(t,1)) && (indicator1<cdf1(t+1,1))
                C(i,j)=t+1;
                end
            end
        end
        
    end
end

%display(C);

samples=zeros(its,N);

for i11=(2+burnin):M
    for j11=1:N
        samples(i11-1-burnin,j11)=C(i11,j11);
    end
end

end
                
        
        
            
        
        

