#-*-python-mode-*-
from pgen import *
from random import random

chromosome = 1
pop = 'JPT'
fname = hapmap_fname(chromosome,pop)
hds = hapmap_dataset(fname)
print("# chromosome %d; pop %s; ignoring SNPs w/ missing values" \
      % (chromosome, pop))
print("# data file:", fname)
print("Printing expected and observed heterozygosity/SNP")

print("%4s %4s" % ("E[H]", "H"))
for snp in hds:
    p = 0.5*snp.mean
    twon = 2.0*len(snp)
    eh = 2*p*(1-p)*twon/(twon-1.0)
    h = snp.gtype.count(1)/float(len(snp.gtype))
    # Use this code for jittering
    # jx = 0.05*(random() - 0.5)
    # jy = 0.05*(random() - 0.5)
    # print "%4.3f %4.3f" % (eh+jx, h+jy)

    # This code for no jittering
    print("%4.3f %4.3f" % (eh, h))
