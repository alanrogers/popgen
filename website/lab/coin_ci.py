from pgen import bnldev

xobs = 5070  # Observed value of statistic.
nreps = 1000 # Number of repetitions to do.

for p in [0.49, 0.495, 0.5, 0.505, 0.51, 0.515, 0.52, 0.525]:
    F = 0.0

    for i in range(nreps):
        x = bnldev(10000, p)
        if x <= xobs:
            F += 1

    F /= nreps

    print("F[%d] = %6.3f for hypothesis: p=%5.3f" % (xobs, F, p))
