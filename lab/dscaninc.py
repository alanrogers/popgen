# dscan.py (incomplete version)
from pgen import hapmap_dataset, hapmap_fname, scatsmooth
from math import sqrt
from random import randrange

nreps = 50
chromosome = 21
pop = 'CEU'
window = 200 # window size in kb

# Return abs(d)
def get_d(snp_x, snp_y):
    # YOUR CODE GOES HERE.
    return 0.0

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

print("Chromosome %d pop %s; %d focal SNPs, %d values of |d|" % \
    (chromosome, pop, nreps, len(distvec)))

# YOUR CODE GOES HERE
