from random import random

# number of simulated data sets
nReps = 1000

data = ['AA', 'TT', 'TT', 'AA', 'TA', 'TT', 'AA', 'TA']

# number of diploid individuals
n = len(data)

# Observed allele frequency and heterozygosity
p = 0
hetz = 0
for genotype in data:
	p += genotype.count('A')
	if genotype[0] != genotype[1]:
		hetz += 1
hetz /= float(n)
p /= float(2*n)

print("p =", p, "Observed heterozygosity =", hetz)

# ltail counts number of times simulated heterozygosity is
# less than or equal to that observed.
ltail = 0

# Look at nReps simulated data sets.
for rep in range(nReps):
    rhetz = 0
    # Loop over individuals in population
    for i in range(n):
	# Draw two independent variates u, and v.
	# Each equals 'A' or 'T' with probs p and 1-p.
        if random() <= p:
            u = 'A'
        else:
            u = 'T'
        if random() <= p:
            v = 'A'
        else:
            v = 'T'
        if u != v:  # count a heterozygote
            rhetz += 1
    rhetz /= float(n)
    if rhetz <= hetz:
        ltail += 1

ltail = float(ltail)/nReps
print("Cumulative distribution: F(%f)=%f" %\
      (hetz, ltail))
