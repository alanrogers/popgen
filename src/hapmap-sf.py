from tabulator import Tabulator
# This program reads a file containing hapmap genotype data and
# calculates the site frequency distribution

# Open data file and read it into a list of lines.
list_of_lines = open("encode-chr7-1Mbp.dat").readlines()

tab = Tabulator(-0.00001, 1.00001, 5)
nmap = {}

# Operate on the lines in the list, one at a time.
for line in list_of_lines:
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

	# Data begins with field 11
	data = line[11:]

        # Make data a list of allelic states
        data = ''.join(data)

	# Strip missing values
	data = data.replace('N','')

        # Make a set of allelic states
        s = set(data)

        # Tabulate number of alleles
        nallele = len(s)
        if nallele in nmap:
            nmap[len(s)] += 1
        else:
            nmap[len(s)] = 1

        # skip monomorphic loci
        if nallele < 2:
            continue

        if nallele > 2:
            print(data)

        # Put allelic counts into a list
        counts = []
        for i in s:
            counts.append(data.count(i))

        # Tabulate the minimum relative frequency
        p = min(counts)/float(len(data))
        assert p <= 0.5
        tab += p

print("Distribution of frequency of minor allele")
print(tab)

print("Distribution of number of alleles")
for i in nmap:
    print("%4d %6d" % (i, nmap[i]))
