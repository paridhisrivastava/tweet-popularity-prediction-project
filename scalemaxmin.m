function scaled=scalemaxmin(x,Mx,Mn)
% Scales the data 
% by Aditya S Murthy, Paridhi Srivastava and  Vatsala Singh, RIT
    [m n]=size(x);
    mx=repmat(Mx,m,1);
    mn=repmat(Mn,m,1);
    scaled=(x-mn)./(mx-mn);