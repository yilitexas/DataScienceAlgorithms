function E_weights=colormle(A,samples)

size_A=size(A);
N1=size_A(1);
size_samples=size(samples);
M1=size_samples(1);
k1=max(samples(:));

p_empirical=zeros(N1,k1);

for j=1:N1
    count1=zeros(k1,1);
    for i=1:M1
            
        for r=1:k1
            if (samples(i,j)==r)
                count1(r,1)=count1(r,1)+1;
            end
        end
    end
    
    count1=count1/M1;
        
    for t=1:k1
        p_empirical(j,t)=count1(t,1);
    end
end

%display(p_empirical);


E_weights=ones(1,k1);

function M_phi=mphi(E)

    M_phi=zeros(1,k1);

    for j=1:k1
        M_phi(1,j)=exp(E(1,j));
    end
end

function E_r=ereverse(Mph)
    E_r=zeros(1,k1);
    
    for j=1:k1
        E_r(1,j)=log(Mph(1,j));
    end
    
end


step=0.1;

p_inference1=zeros(N1,k1);
gradient=zeros(N1,k1);
M_phi2=zeros(N1,k1);
M_phi3=zeros(1,k1);

for repeats=1:10000
    M_phi1=mphi(E_weights);
    %display(M_phi1);
    
    for i=1:N1
        for j=1:k1
            M_phi2(i,j)=M_phi1(1,j);
        end
    end
    
    %display(M_phi2);
            
    p_inference1=sumprod_HW4(A,E_weights,11);
    %display(p_inference1);
    p_difference=p_empirical-p_inference1;
    %display(p_difference);
    gradient=(step*p_difference)./M_phi2;
    %display(gradient);
    M_phi2=M_phi2+gradient;
    %display(M_phi2);
    
    for i=1:k1
        M_phi3(1,i)=mean(M_phi2(:,i));
    end
    
    %display(M_phi3);
    
    E_weights=ereverse(M_phi3);
    %display(E_weights);
end

display(E_weights);

display(p_empirical);

display(p_inference1);

end

