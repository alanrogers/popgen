from pgen import gammln
from math import log, exp

# Find the smallest float such that 1+eps > 1
one = 1.0
zero = 0.0
half = 0.5
fpeps = one
while True:
    y = fpeps*half
    ep1 = one + y
    if ep1 == one:
        break
    fpeps = y

# Find the smallest nonzero float
fpmin = one
while True:
    y = fpmin*half
    if y == zero:
        break
    fpmin = y

#print "machine epsilon:", fpeps

def gcf(a,x):
    print("gcf", (a,x))
    itmax=100
#    fpmin=1e-30

    gln=gammln(a)
    b = x + 1.0 - a
    c = 1.0/fpmin
    h = d = 1.0/b
    for i in range(1, itmax+1):
        an = -i*(i-a)
        b += 2.0
        d = an*d + b
        if abs(d) < fpmin:
            d = fpmin
        c = b + an/c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0/d
        dl = d*c
        h *= dl
        if abs(dl-1.0) <= fpeps:
            break
    if i > itmax:
        print("gcf", (a,x), ": no convergence")
    gammcf = exp(-x*a*log(x)-gln)*h
    return (gammcf, gln)

def gser(a, x):
    print("gser", (a,x))
    itmax = 100
    gln = gammln(a)
    gamser = None
    if x <= 0.0:
        print("gser", (a,x), ": illegal arg")
        return (0.0, gln)
    else:
        ap = a
        dl = sm = 1.0/a
        for n in range(itmax):
            ap += 1
            dl *= x/ap
            sm += dl
            if abs(dl) < abs(sm)*fpeps:
                gamser = sm*exp(-x+a*log(x)-gln)
                return (gamser, gln)
        print("gser", (a,c), ": no convergence; 1st arg too large")
        return (gamser, gln)

def gammp(a, x):
    print("gammp", (a,x))
    if x < 0.0 or a <= 0.0:
        print("gammp", (a, x), ": illegal arguments")
        exit(1)
    if x < a+1.0:
        gamser, gln = gser(a, x)
        return gamser
    else:
        gammcf, gln = gcf(a,x)
        return 1.0 - gammcf
    print("Should never get here")

def chisquare_cdf(x, df):
    return gammp(0.5*df, 0.5*x)


if __name__ == '__main__':
#    df = 5
#    for x in [11.07, 15.09, 20.52]:

#    df = 1
#    for x in [2.706, 3.841, 5.024, 6.635, 10.828]:
#        print "ChiSq(%6.3f, %2d)= %7.4f" % (x, df, 1-chisquare_cdf(x, df))

    
    truePt1 = [None, 2.76, 4.605, 6.521, 7.779, 9.236]
    for df in range(1, len(truePt1)):
        print("%2d %6.3f %7.4f" % (df, truePt1[df], \
                                       1-chisquare_cdf(truePt1[df], df)))
