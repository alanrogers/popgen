from pgen import bnldev

twoN = 100     # population size (number of gene copies)
maxgen = 100000 # maximum number of generations

print("%9s %6s %6s %6s %8s" % ("u", "theta", "E[H]", "H", "g"))
for u in [1e-4, 1e-3, 1e-2, 1e-1]:

    p = 0.5       # initial frequency of allele A
    H = 2*p*(1-p) # initial heterozygosity
    g = 0       # count generations
    theta = 2*twoN*u
    EH = theta/(2*theta + 1)

    # Loop continues until heterozygosity is exhausted
    while H > 0 and g < maxgen:
        p = (1-u)*p + u*(1-p)
        x = bnldev(twoN, p)  # sample from binomial distribution

        p = float(x)/twoN
        H = 2*p*(1-p)
        g += 1

    print("%9.3e %6.3f %6.3f %6.3f %8d" % (u, theta, EH, H, g))
        
