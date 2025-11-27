from pgen import hapmap_dataset, hapmap_fname, expmovav, charplot
from math import sqrt
from random import randrange

nreps = 100
chromosome = 10
pop = 'CEU'
window = 100000

def var(xvec):
    """
    Return variance of vector xvec.
    """
    m = v = 0.0
    for x in xvec:
        m += x
        v += x*x
    n = float(len(xvec))
    m /= n
    v /= n
    v -= m*m
    return v

def cov(xvec, yvec):
    """
    Return covariance of xvec and yvec
    """
    mx = my = mxy = 0.0
    for x, y in zip(xvec, yvec):
        mx += x
        my += y
        mxy += x*y
    n = float(len(xvec))
    mx /= n
    my /= n
    mxy /= n

    cxy = mxy - mx*my
    return cxy

hds = hapmap_dataset(hapmap_fname(chromosome,pop))

data = []
for rep in range(nreps):
    i = randrange(len(hds)) # index of random snp
    snp_x = hds[i]
    vx = var(snp_x.gtype)
    j = i+1
    while j < len(hds):
        snp_y = hds[j]
        dist = snp_y.position - snp_x.position
        if dist > window:
            break
        vy = var(snp_y.gtype)
        cxy = cov(snp_x.gtype, snp_y.gtype)
        abs_r = abs(cxy/sqrt(vx*vy))
        data.append([dist, abs_r])
        j += 1
        
data.sort()  # sorts by dist
dvec = [item[0] for item in data]
rvec = [item[1] for item in data]

rsmooth = expmovav(rvec, 0.85)
print("Smoothed |r|: chromosome %s pop %s" % (chromosome, pop))
charplot(dvec, rsmooth)
