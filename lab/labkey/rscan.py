#!/usr/bin/python
from pgen import *
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

# Get rsq from two SNPs
def get_rsq(snp_x, snp_y):
    cxy = cov(snp_x, snp_y)
    rsq = cxy*cxy
    vxvy = snp_x.variance * snp_y.variance
    if vxvy > 0:
        rsq /= vxvy
    return rsq

hds = hapmap_dataset(hapmap_fname(chromosome,pop))

distvec = []
rsqvec = []
for rep in range(nreps):
    i = randrange(len(hds) - window) # index of random snp
    # scan right
    for j in range(i+1, len(hds)):
        kilobases = abs(hds[j].position - hds[i].position)*0.001
        if kilobases > window:
            break
        distvec.append(kilobases)
        rsqvec.append( get_rsq(hds[i], hds[j]) )

bin_dist, bin_rsq, bin_n = scatsmooth(distvec, rsqvec, 20, 0, window)

print("Chromosome %d pop %s; %d focal SNPs, %d values of rsq" % \
    (chromosome, pop, nreps, len(rsqvec)))

print("%7s %7s %7s" % ("dist", "rsq", "n"))
for dd, bb, nn in zip(bin_dist, bin_rsq, bin_n):
    print("%7.3f %7.3f %7d" % (dd, bb, nn))

charplot(bin_dist, bin_rsq)

