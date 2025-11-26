#!/usr/bin/python
# SNP_tab.py 11 nov 08 associations of neighboring HapMap SNPs
from pgen import *
from math import sqrt
from random import randrange

def cov(xvec, yvec):
    mx = my = mxy = 0.0
    assert len(xvec) == len(yvec)
    for x, y in zip(xvec, yvec):
        mx += x
        my += y
        mxy += x*y
    n = float(len(xvec))
    mx /= n
    my /= n
    mxy /= n

    return mxy - mx*my

chromosome = 22
pop = "JPT"
hds = hapmap_dataset(hapmap_fname(chromosome,pop))

print("\nneighboring SNPs from chromosome %s in %s\n" % (chromosome, pop))

for rep in range(20):
    A = randrange(len(hds)-1) # index of randomly chosen SNP locus A
    B = A + 1                 # index of neighboring SNP locus B
    gtypes_A = hds[A].gtype   # vector of genotypes at A (0,1,2)
    gtypes_B = hds[B].gtype   # vector of genotypes at B (0,1,2)

    table = [[0,0,0],[0,0,0],[0,0,0]]
    for x,y in zip(gtypes_A, gtypes_B):
        table[x][y] += 1

    posA = hds[A].position
    dist = hds[B].position - posA # distance between SNPs (bp)
    print("locus A [rows] (%s/%s) at %d" % \
        (hds[A].alleles[0],hds[A].alleles[1],posA))
    print("locus B [cols] (%s/%s) + %d" % \
        (hds[B].alleles[0],hds[B].alleles[1],dist))
    print(strmat(table))

    varA = hds[A].variance
    varB = hds[B].variance
    covAB = cov(gtypes_A, gtypes_B)
    rD = covAB/sqrt(varA*varB)
    print("rD = %6.3f, rD^2 = %5.3f, n = %d\n" % (rD, rD*rD,len(gtypes_A)))
