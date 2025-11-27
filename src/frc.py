from pylab import plot, show
from math import log10
from lowess import *
from Numeric import *

# Open data file and read it into a list of lines.
list_of_lines = open("encode-chr7-1Mbp.dat").readlines()

focal_position = 126467869 # nucleotide position of focal site
focal_ndx = None           # index of focal site in data

# datmat[i][j] : num copies of allele 0 at site i, individudal j
# posvec[i]    : position on chromosome of site i
datmat = []
posvec = []


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

        # Add this locus to data matrix
        if pos == focal_position:
                focal_ndx = len(datmat) - 1
        for j in range(len(gtype)):
                gtype[j] = gtype[j].count(alleles[0])
        datmat.append(gtype)
        posvec.append(pos)
        curr_loc += 1

nLoci = len(datmat)
assert nLoci == curr_loc
print('End of first pass through data.  Found', nLoci, 'biallelic loci')

if focal_ndx == None:
        print("Didn't find focal position:", focal_position)
        exit(1)
print("focal index:", focal_ndx)

# Count the two types of homozygotes at the focal locus
p = n1 = n0 = 0
for x in datmat[focal_ndx]:
        p += x
        if x == 0:
                # Homozygote for allele 1
                n1 += 1
        elif x == 2:
                # Homozygote for allele 0
                n0 += 1
# p is allele frequency at focal site
p /= 2.0*len(datmat[focal_ndx])
if p < 0.2 or p > 0.8:
        print("ABORTING: allele frequency at focal site is not in [0.2,0.8]")
        exit(1)
if n0==0 or n1 == 0:
        print("ABORTING: Only 1 category of homozygote at focal locus")
        exit(1)
        
# 2nd pass through data:
# Calculate the frequency of recombinant chromosomes (frc)
# separately within each of the two categories of homozygote
# at the focal locus.  
distvec = []
frc0vec = []
frc1vec = []
for curr_loc in range(nLoci):
        #if curr_loc == focal_ndx:
        #       continue

        # distance between current locus and focal locus
        # in kilobases.
        dist = (posvec[curr_loc] - posvec[focal_ndx])/1000.0

        # Calculate the FRC for each category individuals
        # who are homozygous at the focal locus.
        y1 = y0 = 0
        for i, x in enumerate(datmat[focal_ndx]):
                if x == 0:
                        # Homozygote for allele 1
                        y1 += datmat[curr_loc][i]
                elif x == 2:
                        # Homozygote for allele 0
                        y0 += datmat[curr_loc][i]
        frc0 = y0/(2.0*n0)
        frc1 = y1/(2.0*n1)

        # If frc0 > 0.5, then allele 0 is probably not
        # the recombinant allele, so make frc0 the frequency
        # of allele 1.
        if frc0 > 0.5:
                frc0 = 1.0 - frc0
        # The same for the other class of homozygote.
        if frc1 > 0.5:
                frc1 = 1.0 - frc1

        distvec.append(dist)
        frc0vec.append(frc0+0.1)
        frc1vec.append(frc1+0.1)

print("%5s %6s %6s" % ("dist", "frc0", "frc1"))
for i in range(len(distvec)):
        print("%5d %6.4f %6.4f" % (distvec[i],frc0vec[i], frc1vec[i]))

frc0smooth = lowess(array(distvec), array(frc0vec))
frc1smooth = lowess(array(distvec), array(frc1vec))
plot(distvec, frc0vec, 'bo')
plot(distvec, frc1vec, 'r+')
plot(distvec, frc0smooth)
plot(distvec, frc1smooth)

show()
