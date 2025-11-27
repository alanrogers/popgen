from pylab import plot, show
from lowess import *
from Numeric import *

# Open data file and read it into a list of lines.
list_of_lines = open("encode-chr7-1Mbp.dat").readlines()

focal_position = 126467869 # nucleotide position of focal site
focal_ndx = None           # index of focal site in data

# datmat[i][j] : num copies of allele 0 at site i, individudal j
# posvec[i]    : position on chromosome of site i
# sumx[i]      : sum of values in row i of datmat
datmat = []
posvec = []
sumx   = []


# First pass through data: set focal_ndx, posvec, and datmat
curr_loc = 0
for lineno, line in enumerate(list_of_lines):
        # Get rid of white space at beginning and end
        line = line.strip()

        # Skip comments
        if line[0] == '#':
                continue

        # Turn line into a list of fields.
        line = line.split()

        # Skip header
        if line[0] == "rs#":
                continue

        # Position is in field 3
        pos = int(line[3])

        # Genotypes begin with field 11
        gtype = line[11:]

        # get list of alleles at this locus
        alleles = ''.join(set(''.join(gtype)))
        
        # Skip loci with missing values and those with more
        # than 2 alleles.
        if 'N' in alleles or len(alleles) != 2:
                if pos == focal_position:
                        print("Error: can't skip focal position")
                        exit()
                continue

        if pos == focal_position:
                focal_ndx = curr_loc

        # Add this locus to data vectors
	s = 0.0
        for j in range(len(gtype)):
		c = gtype[j].count(alleles[0])
                gtype[j] = c
		s += c
	sumx.append(s)
        datmat.append(gtype)
        posvec.append(pos)
        curr_loc += 1

nLoci = len(datmat)
assert nLoci == curr_loc
print('End of first pass through data.  Found', nLoci, 'biallelic loci')
nPeople = len(datmat[0])
print("Found", nPeople, "people")

if focal_ndx == None:
        print("Didn't find focal position:", focal_position)
        exit(1)
print("focal index:", focal_ndx)

pA = sumx[focal_ndx]/(2.0*nPeople)
qA = 1.0-pA

# 2nd pass through data:
# Calculate of each locus w/ focal locus
distvec = []
Dvec = []
Dprimevec = []
rvec = []
for curr_loc in range(nLoci):
        # distance between current locus and focal locus
        # in kilobases.
        dist = (posvec[curr_loc] - posvec[focal_ndx])/1000.0

        # Calculate sum of x*y
        sumxy = 0
        for x, y in zip(datmat[focal_ndx], datmat[curr_loc]):
		sumxy += x*y

	# Variances and Covariances
	sx = float(sumx[focal_ndx])
	sy = float(sumx[curr_loc])
	mx = sx/nPeople
	my = sy/nPeople
	Cxy = sumxy/float(nPeople) - mx*my
	D = Cxy/2.0

	pB = sy/(2.0*nPeople) # allele freq at curr_loc
	qB = 1.0 - pB

	if D < 0:
		Dmin = max(-pA*pB, -qA*qB)
		Dprime = D/Dmin
	else:
		Dmax = min(pA*qB, qA*pB)
		Dprime = D/Dmax

	r = abs(D)/sqrt(pA*qA * pB*qB)

        distvec.append(dist)
        Dvec.append(abs(D))
	rvec.append(r)
	Dprimevec.append(Dprime)

if 0:
	print("%5s %7s %7s %7s" % ("dist", "D", "r", "Dprime"))
	for i in range(len(distvec)):
		print("%5d %7.4f %7.4f %7.4f" % \
		      (distvec[i],Dvec[i], rvec[i], Dprimevec[i]))

if 0:
	smooth = lowess(array(distvec), array(Dvec))
#	plot(distvec, Dvec, 'bo')
elif 0:
	smooth = lowess(array(distvec), array(rvec))
#	plot(distvec, rvec, 'bo')
else:
	smooth = lowess(array(distvec), array(Dprimevec))
	plot(distvec, Dprimevec, 'bo')
plot(distvec, smooth, 'r')


show()
