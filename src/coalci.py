from random import expovariate
from pgen import poidev

u = 0.001    # mutation rate
Sobs = 82    # Observed value of statistic.
nobs = 77    # sample size (number of gene copies)
nreps = 1000 # Number of repetitions to do.

for i in range(16):
    twoN = 2000 + i*1000
    F = 0.0
    for i in range(nreps):
        n = nobs
        tree_length = 0.0 # total branch length
        while n > 1:
            h = n*(n-1.0)/(2.0*twoN) # hazard of a coalescent event
            t = expovariate(h)       # time until next coalescent event
            tree_length += n*t
            n -= 1

        expected_mutations = tree_length*u
        S = poidev(expected_mutations)
        if S <= Sobs:        # Count number of S's that are <= Sobs
            F += 1

    F /= float(nreps)        # Turn count into a fraction.

    print("F[%d] = %6.3f for hypothesis: 2N=%5d" % (Sobs, F, twoN))
