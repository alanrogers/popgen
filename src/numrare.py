# This program calculates the number of copies of the rarer allele

data = ['AA', 'AA', 'AT', 'TA', 'TA', 'AA', 'TA']

# First make a dictionary of allele counts
dnaseq = ''.join(data)
h = {}
for i in set(dnaseq):
    h[i] = dnaseq.count(i)

print(h)

# get a list of the values
counts = [v for v in h.values()]

# the number of copies of the rarest allele
min_count = min(counts)

print("There are", min_count, "copies of the rarest allele")
