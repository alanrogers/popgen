from pgen import *
from random import randrange

reach = 5000
chromosome = 99
pop = "CEU"
focal_position = 136325116  # position of SNP rs4988235

# REPLACE THIS WITH YOUR OWN get_rsq FUNCTION
def get_rsq(snp_x, snp_y):
    return 0.0

# Find average rsq between one SNP (hds[mid]) and all other SNPs that
# are nearby on the chromosome.  Return None if no such SNPs are
# found.  Average will include all SNPs between x-reach and x+reach,
# where x is the position of the SNP at hds[mid]
def window_rsq(hds, mid, reach):
    midsnp = hds[mid]
    lo = hds.find_position(midsnp.position - reach)
    hi = hds.find_position(midsnp.position + reach)
    if lo == hi:             # make sure hi > lo
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

hds = hapmap_dataset(hapmap_fname(chromosome, pop))
focndx = hds.find_position(focal_position)
print("looking for SNP at pos %d; nearest is at %d" \
      % (focal_position, hds[focndx].position))
if focndx == len(hds)-1:
    print("Error: couldn't find focal_position", focal_position)
    exit(1)
rsq_mean_obs = window_rsq(hds, focndx, reach)

print("Mean rsq w/i %d kb of %s: %f" % (round(reach/1000.0), 
                                         hds[focndx].id, rsq_mean_obs))

# From here on, the program should estimate the probability that a
# random region in this chromosome would have as much LD as the region
# around focal_position.

# To get you started, here is how to set up a loop that will examine "nreps"
# different regions, randomly distributed across the chromosome.
tail = 0     # Count replicates >= rsq_mean_obs
nreps = 100
for rep in range(nreps):
    ndx = randrange(len(hds)) # index of a random SNP

    # Your code goes here. It should calculate rsq_mean_sim for ndx,
    # and add 1 to tail if this value is >= rsq_mean_obs

# At the end, divide tail by nreps and print the answer.
