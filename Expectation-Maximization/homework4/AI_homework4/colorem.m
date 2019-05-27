function E_weights2=colorem(A,y,samples2)

size_A2=size(A);
N2=size_A2(1);
size_samples2=size(samples2);
M2=size_samples2(1);
k2=max(samples2(:));
T2=M2*k2;

EM_estimate=ones(1,k2);
complete_samples=zeros(T2,(N2+1));

function r21=phi22(xi)
    r21=exp(EM_estimate(xi));
end

%calculate the pairwise potential function

function r22=psi22(xi,xj)
    if (xi==xj)
        r22=0;
    else
        r22=1;
    end
end

%this function is to take a specific x assignment, then calculate its joint
%probability;

function marg2=marginal2(x)
    total21=1;
    for i21=1:N2
        temp21=x(1,i21);
        temp22=phi22(temp21);
        total21=total21*temp22;
    end
    
    for i22=1:(N2-1)
        for j21=(i22+1):N2
            if (A(i22,j21)~=0)
                temp21=x(1,i22);
                temp22=x(1,j21);
                temp23=psi22(temp21,temp22);
                total21=total21*temp23;
            end
        end
    end
    
    marg2=total21;
end

function E_r2=ereverse2(Mph)
        E_r2=zeros(1,k2);
    
        for j62=1:k2
            E_r2(1,j62)=log(Mph(1,j62));
        end
end

function M_phi5=mphi2(E)
        M_phi5=zeros(1,k2);
            
        for j72=1:k2
            M_phi5(1,j72)=exp(E(1,j72));
        end    
end

for EM_repeats=1:100

    for i31=1:M2
        temp_vector2=samples2(i31,:);
        for i32=1:k2
            temp31=(i31-1)*k2+i32;
            for i33=1:N2
                if (i33~=y)
                    complete_samples(temp31,i33)=temp_vector2(1,i33);
                else
                    complete_samples(temp31,i33)=i32;
                end
            end
        end
    
        temp_prob2=zeros(1,k2);
        temp_sum2=0;
        for i34=1:k2
            temp_vector2(1,y)=i34;
            temp_prob2(1,i34)=marginal2(temp_vector2);
            temp_sum2=temp_sum2+temp_prob2(1,i34);
        end
        temp_prob2=temp_prob2/temp_sum2;

        for i35=1:k2
            temp32=(i31-1)*k2+i35;
            complete_samples(temp32,(N2+1))=temp_prob2(1,i35);
        end
    end

    %display(complete_samples);
   

    p_empirical2=zeros(N2,k2);

    for j4=1:N2
        count4=zeros(1,k2);
        for i4=1:T2
            
            for r4=1:k2
                if (complete_samples(i4,j4)==r4)
                    count4(1,r4)=count4(1,r4)+complete_samples(i4,(N2+1));
                end
            end
        end
    
        count4=count4/M2;
        
        for t4=1:k2
            p_empirical2(j4,t4)=count4(1,t4);
        end
    end

    %display(p_empirical2);


    E_weights2=ones(1,k2);

    step=0.1;

    p_inference21=zeros(N2,k2);
    gradient2=zeros(N2,k2);
    M_phi22=zeros(N2,k2);
    M_phi23=zeros(1,k2);

    for repeats=1:1000
        M_phi21=mphi2(E_weights2);
        %display(M_phi21);
    
        for i2=1:N2
            for j2=1:k2
                M_phi22(i2,j2)=M_phi21(1,j2);
            end
        end
    
        %display(M_phi22);
            
        p_inference21=sumprod_HW4(A,E_weights2,11);
        %display(p_inference21);
        p_difference2=p_empirical2-p_inference21;
        %display(p_difference2);
        gradient2=(step*p_difference2)./M_phi22;
        %display(gradient2);
        M_phi22=M_phi22+gradient2;
        %display(M_phi22);
    
        for i=1:k2
            M_phi23(1,i)=mean(M_phi22(:,i));
        end
    
        %display(M_phi23);
    
        E_weights2=ereverse2(M_phi23);
        %display(E_weights2);
    end

    %display(E_weights2);

    %display(p_empirical2);

    %display(p_inference21);

    EM_estimate=E_weights2;

end

display(E_weights2);

display(p_empirical2);

display(p_inference21);


end



