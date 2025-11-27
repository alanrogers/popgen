# Gene flow and genetic drift
from pgen import bnldev

twoN = 100      # population size (number of gene copies)
maxgen = 100000 # maximum generation count

p1 = 0.5       # initial frequency of allele A in pop 1
p2 = 0.5       # initial frequency of allele A in pop 1
H1 = 2*p1*(1-p1) # initial heterozygosity
H2 = 2*p2*(1-p2) # initial heterozygosity
m = 0        # rate of gene flow
gen = 0       # count generations

# Loop continues until heterozygosity is exhausted
while H1*H2 > 0.0:
    new_p1 = p1*(1.0-m) + m*p2
    new_p2 = p2*(1.0-m) + m*p1
    x1 = bnldev(twoN, new_p1)  # sample from binomial distribution
    x2 = bnldev(twoN, new_p2)  # sample from binomial distribution

    p1 = float(x1)/twoN
    p2 = float(x2)/twoN
    H1 = 2*p1*(1-p1)
    H2 = 2*p2*(1-p2)
    gen += 1
    print("%4d %6.2f %6.2f %6.2f %6.2f" % (gen, p1, H1, p2, H2))
