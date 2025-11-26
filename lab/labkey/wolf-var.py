#!/usr/bin/python
from random import random

# Return the variance of the values in xvec
def var(xvec):
    m = msq = 0.0
    for x in xvec:
        m += x
        msq += x*x
    n = float(len(xvec))
    m /= n                 # mean
    msq /= n               # mean square
    return msq - m*m       # variance

w = [3246, 3449, 2897, 2841, 3635, 3932]  # counts from Wolf's white die
r = [3407, 3631, 3176, 2916, 3448, 3422]  # counts from Wolf's red die

Vw = var(w)
Vr = var(r)
tail_w = 0.0   # count number of simulated variances smaller than Vw
tail_r = 0.0   # count number of simulated variances smaller than Vr

print("Var(white):", Vw)
print("Var(red)  :", Vr)

nreps = 1000

for rep in range(nreps):
    count = [0,0,0,0,0,0]           # count[i] is number of times we roll i+1

    for roll in range(20000): # 20000 rolls of a fair die
        spots = int(6*random())     # uniform on [0,1,2,3,4,5]
        count[spots] += 1

    v = var(count)
    if v >= Vw:
        tail_w += 1
    if v >= Vr:
        tail_r += 1

print("A fraction %f of simulated variances is as large as Vw." % (tail_w/float(nreps)))
print("A fraction %f of simulated variances is as large as Vr." % (tail_r/float(nreps)))
    
    
