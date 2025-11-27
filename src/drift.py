from __future__ import division, print_function # not needed for Python 3.x
from pgen import bnldev

twoN = 100      # population size (number of gene copies)
maxgen = 100000 # maximum generation count

p = 0.5       # initial frequency of allele A
H = 2*p*(1-p) # initial heterozygosity
gen = 0       # count generations

# Loop continues until heterozygosity is exhausted
while H > 0:
    x = bnldev(twoN, p)  # sample from binomial distribution

    p = x/twoN
    H = 2*p*(1-p)
    gen += 1
    print("%4d %6.2f %6.2f" % (gen, p, H))
