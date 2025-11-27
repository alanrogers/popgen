from time import clock
from pgen import bnldev
from random import random

nreps = 10000
C = 10
p = 0.4

t0 = clock()
for i in range(nreps):
    x = bnldev(C, p)
t1 = clock()
elapsed = t1 - t0
print("C=%7d Elapsed time = %4.10f " % \
      (C, elapsed))

C *= 10

t0 = clock()
for i in range(nreps):
    x = bnldev(C, p)
t1 = clock()
elapsed = t1 - t0
print("C=%7d Elapsed time = %4.10f " % \
      (C, elapsed))

C *= 10

t0 = clock()
for i in range(nreps):
    x = bnldev(C, p)
t1 = clock()
elapsed = t1 - t0
print("C=%7d Elapsed time = %4.10f " % \
      (C, elapsed))

C *= 10

t0 = clock()
for i in range(nreps):
    x = bnldev(C, p)
t1 = clock()
elapsed = t1 - t0
print("C=%7d Elapsed time = %4.10f " % \
      (C, elapsed))
