#!/usr/bin/python
# hapmapspec.py
# Calculate site frequency spectrum
from pgen import *

chromosome = 22
pop = 'JPT'

hds = hapmap_dataset(hapmap_fname(chromosome,pop))
K = 2*len(hds[0]) # number of gene copies in sample

ospec = (K//2 + 1)*[0]

for snp in hds:
    x = sum(snp)
    if x > K/2:
        x = K - x
    assert(x <= K//2)
    assert(x > 0)
    ospec[x] += 1

S = sum(ospec)  # number of segregating sites
assert(S == len(hds))
a = sum([1/i for i in range(1, K)])
theta = S/a
print("S=%f a=%f theta=%f" % (S, a, theta))
espec = (K//2+1)*[0]
for i in range(1,len(espec)):
    if i == K-i:
        espec[i] = theta/i
    else:    
        espec[i] = theta/i + theta/(K-i)

oehist(ospec[1:], espec[1:], range(1,K//2+1))

