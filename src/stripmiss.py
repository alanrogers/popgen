# Open data file and read it into a list of lines.
list_of_lines = open("hapmap-g6pd.dat").readlines()

# Print data, omitting data lines with missing values
# or where the number of alleles isn't 2.
curr_loc = 0
for line in list_of_lines:
        line = line.strip()
        if line[0] == '#':
		print(line)
                continue
        vec = line.split()

        if vec[0] == "rs#":                   # skip header
		print(line)
                continue

        gtype = vec[11:]                      # genotype data
        alleles = ''.join(set(''.join(gtype))) # list of alleles
        
        # Skip loci with missing values and those with more
        # than 2 alleles.
        if 'N' in alleles or len(alleles) != 2:
                continue

	print(line)
