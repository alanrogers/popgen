from pgen import bnldev

xobs = 5070  # Observed value of statistic.
nreps = 100  # Number of repetitions to do.

p = 0.45     # As assumed by hypothesis.
F = 0.0      # Will hold Pr[X <= xobs]

for i in range(nreps):
    x = bnldev(10000, p) # Number of heads in one experiment
    if x <= xobs:        # Count number of x's that are <= xobs
        F += 1

F /= nreps               # Turn count into a fraction.

print("F[%d] = %6.3f for hypothesis: p=%5.3f" % (xobs, F, p))
