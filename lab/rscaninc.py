from pgen import *
from random import randrange

nreps = 500
chromosome = 22
pop = 'JPT'
window = 200

# DEFINE GET_COV AND GET_RSQ FUNCTIONS HERE

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

print("Chromosome %d pop %s; %d focal SNPs, %d values of rsq" % \
    (chromosome, pop, nreps, len(rsqvec)))

# YOUR CODE GOES HERE
