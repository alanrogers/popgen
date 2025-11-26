#!/usr/bin/python
from pgen import *
from random import choice

chromosome = 22
pop = 'JPT'

hds = hapmap_dataset(hapmap_fname(chromosome,pop))
ohvec = [0.7]
ehvec = [0.7]
for i in range(200):
    snp = choice(hds)
    sample_size = len(snp.gtype)
    oh = snp.gtype.count(1)/sample_size
    ohvec.append(oh)
    p = sum(snp.gtype)/(2.0*sample_size)
    eh = 2.0*p*(1.0-p)
    ehvec.append(eh)
    #print "%5.3f %5.3f" % (oh, eh)

charplot(ehvec, ohvec, 50, 40)
