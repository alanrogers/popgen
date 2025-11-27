from pgen import *
#from lowess import *

# Open data file and read it into a list of lines.
list_of_lines = open("hapmap-g6pd.dat").readlines()

#focal_position = 153153043 # nucleotide position of focal site
focal_position = 153335055 # nucleotide position of focal site
#focal_position = 153502036 # nucleotide position of focal site
focal_ndx = None           # index of focal site in data

# datmat[i][j] : num copies of allele 0 at site i, individudal j
# posvec[i]    : position on chromosome of site i
# sumx[i]      : sum of values in row i of datmat
datmat = []
posvec = []
mvec   = []
vvec   = []

def DPrime(D, pA, pB):
    """
    Dprime ranges btw 0 and 1 w/ ordinary haplotype data.
    """
    qA = 1.0 - pA
    qB = 1.0 - pB
    if D < 0:
        denom = max(-pA*pB, -qA*qB)
    else:
        denom = min(pA*qB, qA*pB)
    if denom == 0.0:
        return -9.999
    #print "DPrime: D=%g pA=%g pB=%g denom=%g D'=%g" % \
    #      (D, pA, pB, denom, D/denom)
    return (D/denom)

# Tabulate nonnegative integers in x and y
def xtab(x,y):
	nx = ny = 3
	empty_row = ny*[0]
	m = [empty_row[:] for i in range(nx)]
	for xval, yval in zip(x,y):
		m[xval][yval] += 1
	return m

# First pass through data: set focal_ndx, posvec, and datmat
curr_loc = 0
for lineno, line in enumerate(list_of_lines):
        line = line.strip()
        if line[0] == '#':
                continue
        line = line.split()

        if line[0] == "rs#":                   # skip header
                continue

        pos = int(line[3])                     # position on chromosome
        if pos == focal_position:
                focal_ndx = curr_loc
        gtype = line[11:]                      # genotype data
        alleles = ''.join(set(''.join(gtype))) # list of alleles
        
        # Skip loci with missing values and those with more
        # than 2 alleles.
        if 'N' in alleles or len(alleles) != 2:
                if pos == focal_position:
                        print("Error: can't skip focal position")
                        exit()
                continue

        # Add this locus to data vectors
	m = 0.0
	v = 0.0
        for j in range(len(gtype)):
		c = gtype[j].count(alleles[0])
                gtype[j] = c
		m += c
		v += c*c
	n = float(len(gtype))
	m /= n         # mean
	v = v/n - m*m  # variance
	mvec.append(m) # vector of means
	vvec.append(v) # vector of variances
        datmat.append(gtype)
        posvec.append(pos)
        curr_loc += 1

nLoci = len(datmat)
assert nLoci == curr_loc
assert posvec[focal_ndx] == focal_position
print('End of first pass through data.  Found', nLoci, 'biallelic loci')
lines = None
nPeople = len(datmat[0])
print("Found", nPeople, "people")

if focal_ndx == None:
        print("Didn't find focal position:", focal_position)
        exit(1)
print("focal index:", focal_ndx)

pA = 0.5*mvec[focal_ndx] # allele frequency at focal SNP
qA = 1.0-pA

# 2nd pass through data:
# Calculate of each locus w/ focal locus
distvec = []
Dvec = []
Dprimevec = []
rvec = []
fvec = []
for curr_loc in range(nLoci):
        # distance between current locus and focal locus
        # in kilobases.
        dist = (posvec[curr_loc] - posvec[focal_ndx])/1000.0

        # Calculate sum of x*y
        sumxy = 0
        for x, y in zip(datmat[focal_ndx], datmat[curr_loc]):
		sumxy += x*y

	# Covariance and D
	mx = mvec[focal_ndx]
	my = mvec[curr_loc]
	pB = 0.5*my          # allele freq at curr_loc
	qB = 1.0 - pB

	# Covariance has expectation 2D(1+f)
	# Correlation has expectation r = D/sqrt(pA*qA*pB*qB)
	Cxy = sumxy/float(nPeople) - mx*my
	r = Cxy/sqrt(vvec[focal_ndx]*vvec[curr_loc])
	D = r*sqrt(pA*(1.0-pA)*pB*(1.0-pB))

	# Estimate f, deviation from Hardy-Weinberg
	f = vvec[curr_loc]/(2.0*pB*qB) - 1
	fvec.append(f)

	Dprime = DPrime(D, pA, pB)

	# Debugging output
	if Dprime > 1.9:
		xt = xtab(datmat[focal_ndx], datmat[curr_loc])
		print("Dprime=%g gtype counts:" % Dprime)
		print("   %2d %2d %2d" % (0, 1, 2))
		print("  ----------")
		for j in range(len(xt)):
			print("%d |%2d %2d %2d|" % \
			      (j, xt[j][0], xt[j][1], xt[j][2]))

        distvec.append(dist)
	Dprimevec.append(Dprime)

if 0:
	print("%5s %7s" % ("dist", "Dprime"))
	for i in range(len(distvec)):
		print("%5d %7.4f" % (distvec[i], Dprimevec[i]))

#charplot(distvec, Dprimevec)

Dp_sm = expmovav(Dprimevec)
print("Smoothed D'")
charplot(distvec, Dp_sm, 5, 24, 65)


f_sm = expmovav(fvec)
print("Smoothed f")
charplot(distvec, f_sm, 5, 24, 65)
