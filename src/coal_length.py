n = 30    # sample size (number of gene copies)
C = 1000  # population size (number of gene copies)

from random import expovariate

# Tree length is the sum of the lengths of all the
# branches in the tree.
tree_length = 0.0

# Each pass through loop deals with one coalescent interval.
while n > 1:
    h = n*(n-1.0)/(2.0*C)    # hazard of a coalescent event
    t = expovariate(h)       # time until next coalescent event
    tree_length += n*t
    n -= 1

print("Total branch length: %6.3f generations" % tree_length)
