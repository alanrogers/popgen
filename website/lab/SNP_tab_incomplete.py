# SNP_tab.py   11 nov 08   associations of neighboring HapMap SNPs
from pgen import *
from math import sqrt
from random import randrange

def var(xvec):
    sx = sxx = 0.0
    for x in xvec:
        sx  += x
        sxx += x*x
    n = float(len(xvec))
    v = sxx/n - (sx/n)*(sx/n)
    return v

def cov(xvec, yvec):
    sx = sy = sxy = c = 0.0
    # for x,y in zip(xvec, yvec):
        # YOUR CODE HERE, TO CALCULATE THE COVARIANCE c
    return c

chromosome = 22
pop = "CEU"
hds = hapmap_dataset(hapmap_fname(chromosome,pop))

print("\nneighboring SNPs from chromosome %s in %s\n" % (chromosome, pop))

for rep in range(10):
    A = randrange(len(hds)-1)     # index of SNP locus A
    B = A + 1                     # index of SNP locus B
    gtypes_A = hds[A].gtype       # vector of genotypes at A (0,1,2)
    gtypes_B = hds[B].gtype       # vector of genotypes at B (0,1,2)

    table = [[0,0,0] for i in range(3)]
    for x,y in zip(gtypes_A, gtypes_B):
        table[x][y] += 1

    posA = hds[A].position
    dist = hds[B].position - posA   # distance between SNPs (bp)
    print("locus A [rows] (%s/%s) at %d" % (hds[A].alleles[0],hds[A].alleles[1],posA))
    print("locus B [cols] (%s/%s) + %d" % (hds[B].alleles[0],hds[B].alleles[1],dist))
    print(strmat(table))
    
    varA  = var(gtypes_A)
    varB  = var(gtypes_B)
    covAB = cov(gtypes_A, gtypes_B)
    rD    = covAB/sqrt(varA*varB)
    print("rD = %6.3f, rD^2 = %5.3f, n = %d\n" % (rD, rD*rD,len(gtypes_A)))
