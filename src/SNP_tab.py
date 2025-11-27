# SNP_tab.py   11 nov 08   associations of neighboring HapMap SNPs

from pgen import *
from math import sqrt
from random import randrange

chromosome = 22
pop = "CEU"
nreps = 10

def var(xvec):
    sx = sxx = 0.0
    for x in xvec:
        sx  += x
        sxx += x*x
    n = float(len(xvec))
    v = (sxx - sx*sx/n)/(n-1.0)
    return v

def cov(xvec,yvec):
    sx = sy = sxy = 0.0
    for x,y in zip(xvec,yvec):
        sx += x
        sy += y
        sxy += x*y
    n = float(len(xvec))
    c = (sxy - sx*sy/n)/(n-1.0)
    return c

hds = hapmap_dataset(hapmap_fname(chromosome,pop))
print("")

for rep in range(nreps):
    A = randrange(len(hds)-1)     # index of SNP locus A
    B = A + 1                     # index of SNP locus B
    gtypes_A = hds[A].gtype       # vector of genotypes at A (0,1,2)
    gtypes_B = hds[B].gtype       # vector of genotypes at B (0,1,2)

    table = [[0,0,0] for i in range(3)]
    for x,y in zip(gtypes_A, gtypes_B):
        table[x][y] += 1

    Apos = hds[A].position
    dist = hds[B].position - Apos   # distance between SNPs (bp)
    print("locus A [rows] (%s/%s) at %d" % (hds[A].alleles[0],hds[A].alleles[1],hds[A].position))
    print("locus B [cols] (%s/%s)  + %d" % (hds[B].alleles[0],hds[B].alleles[1],dist))
    print(strmat(table))
    
    varA  = var(gtypes_A)
    varB  = var(gtypes_B)
    covAB = cov(gtypes_A, gtypes_B)
    rAB   = covAB/sqrt(varA*varB)
    print("rAB = %6.3f, r^2 = %5.3f, n = %d\n" % (rAB, rAB*rAB,len(gtypes_A)))
