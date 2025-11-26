from random import expovariate
K = 30       # sample size (number of gene copies)
twoN = 1000  # population size (number of gene copies)

tree_depth = 0.0 # age of last common ancestor in generations

# Each pass through loop deals with one coalescent interval.
while K > 1:
    h = K*(K-1)/(2.0*twoN) # hazard of a coalescent event
    t = expovariate(h)       # time until next coalescent event
    tree_depth += t
    print("%2d %7.2f %7.2f     REMOVE ME" % (K, t, tree_depth))
    K -= 1                   # must be the last line in the loop

print("Tree depth:", tree_depth, "generations")
