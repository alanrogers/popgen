# gtype is a dummy data set: a list of genotypes.  You will get real
# data in exactly this format later in the course.  Each entry in
# the list is the genotype of a different individual.  The 'N'
# is a missing value.
gtype = ['AA', 'AA', 'AT', 'TA', 'TA', 'NT', 'AA', 'TA']

# The simple way to calculate genotype frequencies.  The frequencies
# go into a dictionary called "h".  After the calculation, h['AA'] is
# the number of copies of genotype 'AA' in the data.
h = {}
for i in set(gtype):
    if 'N' in i:    # Skip genotypes that include 'N's (missing
        continue    # values).
    h[i] = gtype.count(i)
print(h)
    
# In order to use the same trick for calculating allele frequencies,
# we first stick the genotypes together into a single character
# string, which I call dnaseq.
dnaseq = ''.join(gtype)
h = {}
s = set(dnaseq) # set of allelic states
s.discard('N')  # remove missing values
for i in s:
    h[i] = dnaseq.count(i)
print(h)


