from random import random
from pgen import bnldev

N = 5          # Number of trials in each binomial deviate.
p = 0.4        # Probability of "success" on each trial.
numreps = 1000 # Number of binomial variates to draw.

xcount = (N+1)*[0]  # counts for "old fashioned" method
ycount = (N+1)*[0]  # counts for bnldev

for i in range(numreps):
    # Old fashioned method
    x = 0
    for j in range(N):
        if random() <= p:
            x += 1
    xcount[x] += 1

    # New method
    y = bnldev(N,p)
    y = int(round(y))
    ycount[y] += 1

print("xcount:", xcount)
print("ycount:", ycount)
