from __future__ import division, print_function # not needed for Python 3.x
from pgen import bnldev

twoN = 100      # population size (number of gene copies)
maxgen = 100000 # maximum generation count

p = 0.5       # initial frequency of allele A
H = 2*p*(1-p) # initial heterozygosity
g = 0         # count generations

# Loop continues until heterozygosity is exhausted or we reach
# the maximum number of generations.
print("%4s %8s %8s" % ("g", "p", "H"))
while H > 0 and g < maxgen:
    # Draw balls from urn. x is a binomial random
    # variate representing the number of copies of A
    # in the next generation.
    x = bnldev(twoN, p)

    p = x/twoN
    H = 2*p*(1-p)
    g += 1
    print("%4d %8.3f %8.3f" % (g, p, H))
