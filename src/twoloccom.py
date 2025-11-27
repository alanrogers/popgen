# twoloccom.py

# File ../lab/twolocinc.py contains incomplete code that
# we gave to students for a lab exercise.  This file contains
# the completed code.
from pgen import mnldev, Tabulator
from math import sqrt

twoN = 5000
s = 0.0001                      # selective advantage of allele A
c = 0.0000001                   # recombination rate
w = [1.0+s, 1.0+s, 1.0, 1.0]  # fitnesses of AB, Ab, aB, & ab

# For tabulating values
tabrsq = Tabulator(0,1,10)
tabd = Tabulator(0,1,10)

print("2N=%d s=%f c=%f" % (twoN, s, c), end=' ')
print("Fitnesses:", w)
trials = 0
ngot = 0
nwant = 50
while ngot < nwant:
    trials += 1
    x = [1.0/twoN, 0, 0.5-1.0/twoN, 0.5] # freqs of AB, Ab, aB, & ab
    pA = x[0] + x[1]
    pB = x[0] + x[2]
    
    while True:
        # adjust x for recombination
        x = [x[0]*(1-c) + c*pA*pB,
             x[1]*(1-c) + c*pA*(1-pB),
             x[2]*(1-c) + c*(1-pA)*pB,
             x[3]*(1-c) + c*(1-pA)*(1-pB)]
        # adjust x for gametic selection.  There is no need to normalize
        # the new x so that it sums to 1.  mnldev does that automatically.
        for i in range(len(x)):
            x[i] *= w[i]

        n = mnldev(twoN, x)    # sample from multinomial
        x = [z/twoN for z in n]
        pA = x[0]+x[1]
        pB = x[0]+x[2]
        if pA==0 or pA>=0.5 or pB==0 or pB==1:
            break

    if (pA >= 0.5) and (0 < pB < 1):
        # r squared
        D = x[0]*x[3] - x[1]*x[2]
        rsq = D*D/(pA*(1-pA)*pB*(1-pB))
        tabrsq += rsq

        # Li and Nei "d"
        d = x[0]/(x[0] + x[1]) - x[2]/(x[2] + x[3])
        tabd += d

        ngot += 1

print(f"Trials: {trials}")
# Tabulations
print("r squared:")
print(tabrsq)
print()
print("d:")
print(tabd)
