clc
clear all


A=[0 1 0 0;
    1 0 1 1;
    0 1 0 0;
    0 1 0 0];
    
 weight=[1,2,3];
    
 gibbs(A,weight,1000,10000);
 
 %note: when the graph is a tree, this script will provide the exact parition function value; when
 %the graph is not a tree, this script only provides an approximation of
 %the exact partition function value.
