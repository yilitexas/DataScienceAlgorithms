clc
clear all


A=[0 1 0 0;
1 0 1 1;
0 1 0 0;
0 1 0 0];
    
    
 weight=[1 2 3];
    
 samples=gibbs_HW4(A,weight,1000,10000);
 
 %display(samples);
 
 E_weights55=colorem(A,2,samples);
 
 
 
 