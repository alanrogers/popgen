# Generate data for graph showing H as a function of theta in a biallelic model
from math import *

def h(theta):
    return(theta/(2*theta+1.0))

lo = 0.001
hi = 100.0
nsteps = 25
step = log10(hi/lo)/float(nsteps-1)

print "\\plot"
print "%%%10s %8s" % ("log10 theta", "H")
for i in range(nsteps):
    theta = 10**(log10(lo) + i*step)
    print " %10.4f %8.4f" % (log10(theta), h(theta))
print "/"
    
