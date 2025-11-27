from pgen import hapmap_dataset, hapmap_fname, expmovav, charplot
from math import sqrt, log, log10
from random import randrange

nreps = 100
chromosome = 2
pop = 'CEU'
halfwindow = 100 # in kb

# Return mean and variance of vector xvec.
def meanvar(xvec):
    m = v = 0.0
    for x in xvec:
        m += x
        v += x*x
    n = float(len(xvec))
    m /= n
    v /= n
    v -= m*m
    return m, v

# Return covariance of xvec and yvec
def cov(xvec, yvec):
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

def slope(xvec, yvec):
    """
    Return slope of linear regression of yvec on xvec.
    """
    cxy = cov(xvec,yvec)
    mx, vx = meanvar(xvec)
    return cxy/vx

def logit(x):
    x = max(0.01, min(0.99, x))
    return log(x/(1.0-x))

def estimate_ld(gtypeX, pA, qA, vx, gtypeY):
    my, vy = meanvar(gtypeY)
    cxy = cov(gtypeX, gtypeY)
    if cxy < 0:
        # Relabel B and b so cxy > 0
        my = 2 - my
        cxy = -cxy
    pB = 0.5*my
    qB = 1 - pB
    r = cxy/sqrt(vx*vy)
    D = r * sqrt(pA*qA*pB*qB)

    # D is only an estimate and may not be inside the
    # range of legal values.  Next bit coerces D back
    # inside the legal range.
    if D < 0:
        D = max(D, -pA*pB, -qA*qB)
    else:
        D = min(D, pA*qB, qA*pB)
    x = [pA*pB+D, pA*qB-D, qA*pB-D, qA*qB+D]
    assert abs(sum(x)-1.0 < 0.00001)
    pB_A = x[0]/pA # freq of B on A-gametes
    pB_a = x[2]/qA # freq of B on a-gametes
    if 0:
        # Use logit transform
        ld_A = pB_A
        ld_a = logit(pB_a)
        return ld_A, ld_a
    elif 0:
        # No transform
        ld_A = pB_A
        ld_a = pB_a
        return ld_A, ld_a
    else:
        beta = r*sqrt(pB*qB/(pA*qA))
        assert beta>=0, "cxy=%e r=%e D=%e beta=%e" % (cxy, r, D, beta)
        #logbeta = log10(max(beta, 0.001))
        return beta

hds = hapmap_dataset(hapmap_fname(chromosome,pop))

if 0:
    # position of LCT on human chromosome 2
    start = hds.find_position(136261885)
    assert start < len(hds)
    stop = hds.find_position(136311220)
    assert stop < len(hds)
else:
    # whole chromosome
    start = 0
    stop = len(hds)

print("%10s %6s %9s %9s %9s %9s" % \
      ("position", "N", "pA", "s_A/k", "s_a/k", "s_A/s_a"))

for rep in range(nreps):
    i = randrange(start,stop) # index of random snp
    snp_x = hds[i]
    mx, vx = meanvar(snp_x.gtype)
    pA = 0.5*mx
    qA = 1-pA
    j = i+1
    data_A = []
    data_a = []

    # scan right
    for j in range(i+1, len(hds)):
        dist = abs(hds[i].position - hds[j].position)*0.001
        if dist > halfwindow:
            break
        #ld_A, ld_a = estimate_ld(hds[i], pA, qA, vx, hds[j])
        #data_A.append([dist, ld_A])
        #data_a.append([dist, ld_a])
        ld = estimate_ld(hds[i], pA, qA, vx, hds[j])
        data_A.append([dist, ld])

    # scan left
    for j in range(i-1, -1, -1):
        dist = abs(hds[i].position - hds[j].position)*0.001
        if dist > halfwindow:
            break
        #ld_A, ld_a = estimate_ld(hds[i], pA, qA, vx, hds[j])
        #data_A.append([dist, ld_A])
        #data_a.append([dist, ld_a])
        ld = estimate_ld(hds[i], pA, qA, vx, hds[j])
        data_A.append([dist, ld])

    print("************ Got %d SNPs ********************" % len(data_A))
    data_A.sort()
    vec_distA = [item[0] for item in data_A]
    vec_ldA = [item[1] for item in data_A]
    smooth_ldA = expmovav(vec_ldA, 0.85)
    if 0:
        ndx = 0
        for ndx in range(len(smooth_ldA)):
            if smooth_ldA[ndx] <= -1.5:
                break
        smooth_ldA = smooth_ldA[:ndx]
        vec_distA = vec_distA[:ndx]
        vec_ldA = vec_ldA[:ndx]
    #s_A = slope(vec_distA, vec_ldA)
    s_A = slope(vec_distA, smooth_ldA)
    
    print("%10d %6d s/Gb=%9.5f" % \
          (hds[i].position, len(vec_distA), 1000*s_A))
    charplot(vec_distA, smooth_ldA)
    

