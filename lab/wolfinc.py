from random import random

# define a function to return the variance of values in xvec
def var(xvec):
    m = msq = 0.0
    for x in xvec:
        m += x
        msq += x*x
    n = float(len(xvec))
    m /= n                                  # mean
    msq /= n                                # mean square
    return (msq - m*m)                      # variance

w = [3246, 3449, 2897, 2841, 3635, 3932]    # counts from white die
r = [3407, 3631, 3176, 2916, 3448, 3422]    # counts from red die

Vw = var(w)
Vr = var(r)
print("Var(white):", Vw)
print("Var(red)  :", Vr)

nreps = 10                          # adjust this to do more replicates
for rep in range(nreps):
    count = [0,0,0,0,0,0]           # count[i] accumulates the numbers of
                                    #     rolls that showed i+1 spots
    for roll in range(20000):       # do 20000 rolls of the simulated die
        spots = int(6.0*random())   # uniform on [0,1,2,3,4,5]
        count[spots] += 1           # here's the accumulation

    v = var(count)                  # and here's our function call

    print("Repetition %d: var=%f" % (rep, v))    # REMOVE ME later

