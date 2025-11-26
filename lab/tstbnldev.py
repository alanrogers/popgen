from random import random
from pgen import bnldev, charplot

# In each repetition of this experiment, we draw a binomial
# random variable two ways.  First by drawing N uniform random
# values and recording a "success" with probability p.  Then
# by using a canned routine "binldev" that generates binomial
# random variates.  The goal is to see whether these give
# similar answers.

N = 100          # Number of trials in each binomial deviate.
p = 0.4          # Probability of "success" on each trial.
numreps = 1000   # Number of binomial variates to draw.

# Create two lists to hold counts.
# xcount[i] will hold the number of repetitions on which x=i.
# At the start, all entries are 0.
xcount = (N+1)*[0]
ycount = (N+1)*[0]

for i in range(numreps):
    # Draw a binomial random variate the hard way.
    x = 0
    for j in range(N):
        if random() <= p:
            x += 1
    # Now x is a binomial random variate.  Use xcount to count it.
    xcount[x] += 1

    # Draw a binomial random variate the easy way
    y = bnldev(N,p)
    y = int(round(y))
    ycount[y] += 1

# Next step: find out whether the two distributions are equal.
# The easy way to do this involves two steps: (1) turn each
# distribution into a cumulative distribution; (2) plot one
# against the other.

# Make the two distributions cumulative
for i in range(1,len(xcount)):
    xcount[i] += xcount[i-1]
    ycount[i] += ycount[i-1]

# Plot one cumulative distribution against the other
charplot(ycount, xcount)

# Is the resulting plot a straight line with slope 1?  If so,
# then the two methods of drawing binomial random variables are
# equivalent.

