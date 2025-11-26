#!/usr/bin/python
from pgen import *
import sys
from random import randrange

#reach = 3000 # in bases
#reach = 5000 # in bases
#reach = 10000
#reach = 20000
#reach = 200000
reach = 1000000 # in bases
chromosome = 2
pop = "CEU"
focal_position = 136325116  # position of SNP rs4988235
focal_rs= "rs4988235"

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

# Find average rsq between one SNP (hds[mid]) and all other SNPs that
# are nearby on the chromosome.  Return None if no such SNPs are
# found.  Average will include all SNPs between x-reach and x+reach,
# where x is the position of the SNP at hds[mid]
def window_rsq(hds, mid, reach):
    midsnp = hds[mid]
    lo = hds.find_position(midsnp.position - reach)
    hi = hds.find_position(midsnp.position + reach)
    if lo == hi:
        return None

    rsqsum = n = 0
    for i in range(lo, hi+1):
        if i == mid:
            continue
        rsq = get_rsq(hds[i], midsnp)
        if rsq != None:
            n += 1
            rsqsum += rsq

    return rsqsum / float(n)

print("Calling hapmap_dataset")
sys.stdout.flush()

hds = hapmap_dataset(hapmap_fname(chromosome, pop))

print("Back fr hapmap_dataset")
sys.stdout.flush()

focndx = hds.find_position(focal_position)
print("looking for SNP %s at pos %d; nearest is %s at %d" \
      % (focal_rs, focal_position, hds[focndx].id,
         hds[focndx].position))
if focndx >= len(hds)-1:
    print("Error: couldn't find focal_position", focal_position)
    exit(1)

rsq_obs = window_rsq(hds, focndx, reach)

print("Mean rsq w/i %d kb of %s: %f" % (round(reach/1000.0),
                                         hds[focndx].id, rsq_obs))

################

tail = 0
nreps = 100

# Examine many random positions w/i chromosome. Count the number of these
# for which rsq is at least as large as observed value.
for rep in range(nreps):

    # Get a random value of rsq
    ndx = randrange(len(hds))
    rsq = window_rsq(hds, ndx, reach)

    # Increment tail counter
    if rsq >= rsq_obs:
        tail += 1

    # Print something so user knows things are working.
    if rep%20==0:
        print("rep %4d upper tail = %5.3f" % (rep, tail/float(rep+1)))
        sys.stdout.flush()

tail /= float(nreps)

print("Upper tail prob:", tail, "based on", nreps, "repetitions")

