from math import exp

for twoNs in [-10, -1, -0.1, 0.1, 1, 10.0]:
    print "%% 2Ns = %f" % twoNs
    denom = (1 - exp(-twoNs))
    print "\\plot"
    for i in range(1,100):
        p = i/100.0
        pi1 = (1 - exp(-twoNs*p))/denom
        print "%5.2f %10.8f" % (p, pi1)
    print "/"

