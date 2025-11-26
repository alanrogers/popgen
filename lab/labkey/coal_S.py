#!/usr/bin/python
from random import expovariate
from pgen import poidev

twoN = 5000  # population size (number of gene copies)
u = 0.001    # mutation rate

for i in range(20):
    K = 77       # sample size (number of gene copies)
    tree_length = 0.0 # total branch length

    # Each pass through loop deals with one coalescent interval.
    while K > 1:
        h = K*(K-1)/(2.0*twoN) # hazard of a coalescent event
        t = expovariate(h)       # time until next coalescent event
        tree_length += K*t
        K -= 1

        print("Tree length:", tree_length, "generations")
        expected_mutations = tree_length*u
        print("expected mutations:", expected_mutations)
        S = poidev(expected_mutations)
        print("S:", S)
