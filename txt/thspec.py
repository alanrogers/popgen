from __future__ import division, print_function
def thetaS(S, K):
     return S/sum(1/i for i in range(1,K))

def foldedspec(theta, i, K):
     if i < K/2:
          s = theta/i + theta/(K-i)
     elif i == K/2:
          s = theta/i
     return s

S = 31
K = 20
theta = thetaS(S, K)

for i in range(1,K//2 + 1):
    print("%2d %7.5f" % (i, foldedspec(theta, i, K)))

