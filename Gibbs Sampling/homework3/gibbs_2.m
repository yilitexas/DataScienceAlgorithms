function m=gibbs_2(A,w,burnin,its)

size1=size(A);
size_w=size(w);
k=size_w(2);
N=size1(1);

M=1+burnin+its;
C=zeros(M,k);

C(1,1)=1;
C(1,2)=2;
C(1,3)=2;
C(1,4)=3;
%display(C);

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

display(C);

Ma=zeros(N,k);

for j=1:N
    count1=zeros(k,1);
    for i=(2+burnin):M
            
        for r=1:k
            if (C(i,j)==r)
                count1(r,1)=count1(r,1)+1;
            end
        end
    end
    
    count1=count1/its;
        
    for t=1:k
        Ma(j,t)=count1(t,1);
    end
end

display(Ma);
        
        













end
                
        
        
            
        
        

