# This program calculates heterozygosity from genotype data

# The list "data" is a dummy data set: a list of genotypes.  You will
# soon get real data in exactly this format.  Each entry in the list
# is the genotype of a different individual.
data = ['AA', 'AA', 'AT', 'TA', 'TA', 'AA', 'TA']

# Calculate heterozygosity
heterozygosity = 0
for genotype in data:
	if genotype[0] != genotype[1]:
		heterozygosity += 1
heterozygosity /= float(len(data))
print("Heterozygosity:", heterozygosity, "N:", len(data))

