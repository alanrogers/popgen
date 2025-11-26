#!/usr/bin/python
# dscan.py
from pgen import hapmap_dataset, hapmap_fname, scatsmooth, charplot
from math import sqrt, log, exp
from random import randrange

nreps = 500
chromosome = 22
pop = 'JPT'
window = 200

# Return covariance of xvec and yvec
def cov(xvec, yvec):
    mx = my = mxy = 0.0
    for x, y in zip(xvec, yvec):
        mx += x
        my += y
        mxy += x*y
    n = float(len(xvec))
    mx /= n
    my /= n
    mxy /= n

    return mxy - mx*my 

# Return abs(d)
def get_d(snp_x, snp_y):
    cxy = cov(snp_x, snp_y)
    r = cxy/sqrt(snp_x.variance*snp_y.variance)
    pA = 0.5*snp_x.mean
    qA = 1-pA
    pB = 0.5*snp_y.mean
    qB = 1-pB
    d = abs(r*sqrt(pB*qB/(pA*qA)))
    return d

hds = hapmap_dataset(hapmap_fname(chromosome,pop))

distvec = []
dvec = []
for rep in range(nreps):
    i = randrange(len(hds)) # index of random snp
    for j in range(i+1, len(hds)):
        dist = abs(hds[i].position - hds[j].position)*0.001
        if dist > window:
            break
        distvec.append(dist)
        dvec.append(get_d(hds[i], hds[j]))

bin_dist, bin_d, bin_n = scatsmooth(distvec, dvec, 20, 0, window)

print("Chromosome %d pop %s; %d focal SNPs, %d values of |d|" % \
    (chromosome, pop, nreps, len(distvec)))

print("%7s %7s %7s" % ("dist", "|d|", "n"))
for dd, bb, nn in zip(bin_dist, bin_d, bin_n):
    print("%7.3f %7.3f %7d" % (dd, bb, nn))

