# twolocinc.py
from pgen import mnldev, Tabulator
from math import sqrt

twoN = 500
s = 10/twoN                   # selective advantage of allele A
c = 0.001                     # recombination rate
w = [1.0+s, 1.0+s, 1.0, 1.0]  # fitnesses of AB, Ab, aB, & ab

# Tabulate values in [0,1] into 10 bins
tab = Tabulator(low=0, high=1, nBins=10)

print("2N=%d s=%f c=%f" % (twoN, s, c), end=' ')
print("Fitnesses:", w)
print("%6s %6s %6s" % ("pA", "pB", "rsq"))
trials = 0
ngot = 0
nwant = 50
while ngot < nwant:
    trials += 1
    x = [1.0/twoN, 0, 0.5-1.0/twoN, 0.5] # freqs of AB, Ab, aB, & ab
    pA = x[0]+x[1]
    pB = x[0]+x[2]
    while True:
        # Insert code here to adjust x for recombination
        # Insert code here to adjust x for gametic selection
        n = mnldev(twoN, x)    # sample from multinomial
        x = [z/twoN for z in n]
        pA = x[0]+x[1]
        pB = x[0]+x[2]
        if pA==0 or pA>=0.5 or pB==0 or pB==1:
            break

    if pA >= 0.5 and (0 < pB < 1):
        # Insert code here to calculate rsq.
        rsq = 0.0
        print("%6.3f %6.3f %6.3f" % (pA, pB, rsq))
        tab += rsq
        ngot += 1

print(f"Trials: {trials}")
# Print the tabulation in a readable format.
print(tab)
