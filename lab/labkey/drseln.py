#!/usr/bin/env python3
from random import random
from pgen import bnldev

nreps = 10000 # number of replicates
s = 0.02     # selection for allele 1
h = 0.5
w11 = 1.0 + s
w12 = 1.0 + h*s
w22 = 1.0

for twoN in [500,1000,2000,4000]:
    nFixed = 0
    for rep in range(nreps):
        p = 1.0/twoN
        q = 1.0 - p
        while 0.0 < p < 1.0:
            wbar = p*p*w11 + 2*p*q*w12 + q*q*w22
            new_p = p*(p*w11 + q*w12)/wbar
            p = bnldev(twoN, new_p)/twoN
            q = 1.0 - p
        if p == 1.0:
            nFixed += 1
    print("nreps=%d 2N=%d s=%f sh=%f" % (nreps, twoN, s, s*h))
    print("Fraction fixed: %d/%d = %f" % (nFixed, nreps, float(nFixed)/nreps))
    if s == 0.0:
        print("Expected frac :", 1.0/twoN)
    else:
        print("Expected frac :", 2*h*s)
    print("************")
