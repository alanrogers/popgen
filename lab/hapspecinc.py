# hapspec.py
# Calculate site frequency spectrum
from pgen import *

chromosome = 22
pop = 'JPT'

hds = hapmap_dataset(hapmap_fname(chromosome,pop))
K = 2*len(hds[0]) # number of gene copies in sample

ospec = (K//2 + 1)*[0]

# Calculate ospec by summing across chromosome
for snp in hds:
   # Set x equal to number of copies of minor allele in current snp
   x = 1 # CHANGE ME
   assert x <= K//2
   assert x > 0
   ospec[x] += 1

# Calculate espec

# Use oehist to compare ospec with espec
