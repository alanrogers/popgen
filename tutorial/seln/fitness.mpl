unassign('wbar','q','p','p2','dp','w11','w12','w22');
p2 := (w11*p^2 + w12*p*q)/wbar;
dp := p*q*((w11 - w12)*p  + (w12 - w22)*q)/wbar;
wbar := w11*p^2 + w12*2*p*q + w22*q^2;
q := 1-p;
w11 := 1.0;
w12 := 1.4;
w22 := 0.7;
