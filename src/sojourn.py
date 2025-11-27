from random import random
from pgen import bnldev, Tabulator

nreps = 10000 # number of replicates
twoN = 400    # population size (in gene copies)
s = 5.0/twoN  # selection for allele 1
h = 0.5
w11 = 1.0
w12 = 1.0 - h*s
w22 = 1.0 - s

nlost = genlost = nfixed = genfixed = 0
fixedtab = Tabulator(0,1,10)
losttab = Tabulator(0,1,10)
for rep in range(nreps):
    gen = 0
    curtab = Tabulator(0,1,10)
    p = 1.0/twoN
    q = 1.0 - p
    while 0.0 < p < 1.0:
        gen += 1
        wbar = p*p*w11 + 2*p*q*w12 + q*q*w22
        new_p = p*(p*w11 + q*w12)/wbar
        p = bnldev(twoN, new_p)/float(twoN)
        q = 1.0 - p
        curtab += p
#    print "rep %d: gens=%3d p = %2.0f" % (rep, gen, p)
    if p == 0.0:
            nlost    += 1.0
            genlost  += gen
            losttab.merge(curtab)
    else:
            nfixed    += 1.0
            genfixed  += gen
            fixedtab.merge(curtab)
print("twoN = %d, s = %.4f, h = %.4f, nreps = %d" % (twoN, s, h, nreps))
if nlost > 0:
    print("number lost:  %4d;  mean number of generations: %6.1f" \
        % (nlost, genlost/float(nlost)))
if nfixed > 0:
    print("number fixed: %4d;  mean number of generations: %6.1f" \
        % (nfixed, genfixed/float(nfixed)))

print("FixedTab:\n", fixedtab)
print("genfixed:", genfixed)
print("LostTab :\n", losttab)
print("genlost:", genlost)
