# There are two loci, one with alleles A and a, the other with alleles B and b.
# This gives us 4 gamete types: AB, Ab, aB, and ab.
#
# Initially, gamete frequencies are
#
# AB         1/twoN
# Ab          0
# aB          pB - 1/twoN
# ab          1 - pB
#
# where pB is initial frequency of B (see below).
#
# NOTATION
# Gamete     count relFreq  fitness  
#     AB      n[0]    x[0]     w[0]
#     Ab      n[1]    x[1]     w[1]
#     aB      n[2]    x[2]     w[2]
#     ab      n[3]    x[3]     w[3]

from math import sqrt
from random import random
from pgen import mnldev

nLoci = 1000                  # number of repetitions
twoN = 500                    # total population size
s = 0.02                      # selective advantage of allele A
c = 0.001                     # recombination rate
w = [1.0+s, 1.0+s, 1.0, 1.0]  # fitnesses of AB, Ab, aB, & ab

print("#****** TWOLOCSIM *******")
print("# Haploid population size twoN:", twoN)
print("# Selection coefficient:", s)
print("# Recombination rate:", c)
print("# Fitnesses:", w)

print("%4s %6s %6s %6s" % ("rep", "pA", "pB", "rsq"))
for locus in range(0, nLoci):
    x = [1.0/twoN, 0, 0.5-1.0/twoN, 0.5]  # relative freqs
    pA = x[0]+x[1] # rel freq of A
    pB = x[0]+x[2] # rel freq of B
    while True:
        # Adjust x for recombination
        if c > 0:
            x = [x[0]*(1-c) + c*pA*pB,
                 x[1]*(1-c) + c*pA*(1-pB),
                 x[2]*(1-c) + c*(1-pA)*pB,
                 x[3]*(1-c) + c*(1-pA)*(1-pB)]

        # adjust x for gametic selection.  There is no need to normalize
        # the new x so that it sums to 1.  mnldev does that automatically.
        for i in range(0,4):
            x[i] *= w[i]

        # Draw from urn to get next generation
        n = mnldev(twoN, x)
        x = [float(z)/twoN for z in n]
        pA = x[0]+x[1] # rel freq of A
        pB = x[0]+x[2] # rel freq of B
        if pA==0 or pA>=0.5 or pB==0 or pB==1:
            break

    if pA >= 0.5 and (0 < pB < 1):
        D = x[0]*x[3] - x[1]*x[2]
        rsq = D*D/(pA*(1-pA)*pB*(1-pB))
    
        print("%4d %6.3f %6.3f %6.3f" % (locus, pA, pB, rsq))
          

