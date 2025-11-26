from pgen import *
from random import choice

chromosome = 22
pop = 'JPT'
hds = hapmap_dataset(hapmap_fname(chromosome,pop))

for i in range(20):
    snp = choice(hds)
    
    ohet = 0.0  # REPLACE ME
    ehet = 0.0  # REPLACE ME
    
    print("%5.3f %5.3f" % (ohet, ehet))
