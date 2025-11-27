from random import random                                       # line number  1

# define a function to return the variance of values in xvec                #  3
def var(xvec):                                                              #  4
    m = msq = 0.0                                                           #  5
    for x in xvec:                                                          #  6
        m += x                                                              #  7
        msq += x*x                                                          #  8
    n = float(len(xvec))                                                    #  9
    m /= n                                  # mean                          # 10
    msq /= n                                # mean square                   # 11
    return (msq - m*m)                      # variance                      # 12

w = [3246, 3449, 2897, 2841, 3635, 3932]    # counts from white die         # 14
r = [3407, 3631, 3176, 2916, 3448, 3422]    # counts from red die           # 15

Vw = var(w)                                                                 # 17
Vr = var(r)                                                                 # 18
print("Var(white):", Vw)                                                     # 19
print("Var(red)  :", Vr)                                                     # 20

nreps = 10                          # adjust this to do more replicates     # 22
for rep in range(nreps):                                                   # 23
    count = [0,0,0,0,0,0]           # count[i] accumulates the numbers of   # 24
                                    #     rolls that showed i+1 spots       # 25
    for roll in range(20000):      # do 20000 rolls of the simulated die   # 26
        spots = int(6.0*random())   # uniform on [0,1,2,3,4,5]              # 27
        count[spots] += 1           # here's the accumulation               # 28

    v = var(count)                  # and here's our function call          # 30

    print("Repetition %d: var=%f" % (rep, v))    # REMOVE ME later           # 32

