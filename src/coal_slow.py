# coal_slow.py  DIRECT (BUT INEFFICIENT) METHOD

n = 6     # sample size (number of gene copies)
C = 1000  # population size (number of gene copies)

from math import log10
from random import random

tree_depth = gen = 0
h = n*(n-1.0)/(2.0*C)        # hazard of a coalescent event

# Each generation we test for the occurrence of a coalescent event
# When one occurs, we reduce the number of lineages and recalculate h
while n > 1:
    gen += 1
    if random() < h:
        # Note the comma at the end of the 1st print statement.  It
        # combines the two print statements into a single line of
        # output.
        intvl_len = gen - tree_depth
        print("n=%1d 1/h=%6.1f intvl=%4d" % (n, 1.0/h, intvl_len), end=' ')
        print(" log(1/h)=%6.1f log(intvl)=%6.1f" \
              %  (log10(1.0/h), log10(intvl_len)))
        tree_depth = gen
        n -= 1
        h = n*(n-1.0)/(2.0*C)

print("Todal depth of tree:", gen)

