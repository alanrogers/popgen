
# hapmap_site_freq.py  23 September 2008
# observed and expected site frequency spectra of ENCODE intervals

# Open the data file, read it and close it
file_name = \
 "/home/rogers/hapmap/hapmap-r23/genotypes_chr10_CHB_r23a_nr.b36_fwd.txt"

SNP_file = open(file_name,"r")
list_of_lines = SNP_file.readlines()
SNP_file.close()

# A list will hold the "folded" site frequency spectrum
obs_spec = [0 for i in range(100)]
num_lines = len(list_of_lines)
sum_obs = sum_exp = missing = S = 0

# Operate on the lines in the list, one at a time
for line_num in range(1,num_lines):
     # Turn the line into a list of fields (splitting at white space)
     list_of_fields = list_of_lines[line_num].split()
     num_fields = len(list_of_fields)

     # Get the alleles (and skip any sites with more than 2!)
     if len(list_of_fields[1]) > 3:
         print("3 alleles! %s" % (list_of_fields[1]))
         print(list_of_lines[line_num])
         continue
     allele1 = list_of_fields[1][0]
     allele2 = list_of_fields[1][2]

     # Count the numbers of allele1 and allele2 (checking for N)
     tot_allele1 = tot_allele2 = 0
     for individual in range(11, num_fields):
         if list_of_fields[individual][0] == "N":
             missing += 1
             continue
         na1 = list_of_fields[individual].count(allele1)
         na2 = list_of_fields[individual].count(allele2)
         # Increment the totals for this site
         tot_allele1 += na1
         tot_allele2 += na2

     # Is the minor allele frequency greater than zero?
     if tot_allele1 < tot_allele2:
         num_minor_allele = tot_allele1
     else:
         num_minor_allele = tot_allele2

     if num_minor_allele == 0:
         continue

     # OK, then increment the observed spectrum and S, and calculate pi
     obs_spec[num_minor_allele] += 1
     S += 1
     p = float(tot_allele1)/float(tot_allele1+tot_allele2)
     exp_het = 2.0*p*(1.0-p)  # pi = expected heterozygosity
     sum_exp += exp_het       # running sum over all sites

# Now, calculate the EXPECTED FOLDED site frequency spectrum
g = 2*(num_fields - 11)  # the number of gene copies in the sample
a = sum([1.0/float(i) for i in range(1,g)])
theta = float(S)/a
exp_spec = [0 for i in range(g/2 + 1)]
for i in range(1,g/2+1):
     exp_spec[i] = theta/i + theta/(g-i)
exp_spec[g/2] -= theta/(g/2)

# Print the full observed and expected site frequency spectra
print("full site-frequency spectra")
cum_obs = cum_exp = 0
for i in range(1, g/2+1):
     cum_obs += obs_spec[i]
     cum_exp += exp_spec[i]
     print("%2d : %4d  %6.1f  %4d  %6.1f" % (i,obs_spec[i],exp_spec[i],cum_obs,cum_exp))

# Print summary with condensed (grouped) spectra
print()
print("%s contains %d segregating sites" % (file_name, S))
print("%d gene copies, %d missing genotypes\n" % (g, missing))
# pi is the average heterozygosity over all half-million sites
pi = sum_exp/500000.0
print("pi = %7.5f, theta(per site) = %7.5f\n" % (pi,theta/500000.0))

print("Grouped site frequency spectrum:")
print()
print("%5s : %5s %7s" % ("range", "obs", "exp"))
cum_obs = cum_exp = 0
begin_group = 1
for i in range(1, g/2+1):
     cum_obs += obs_spec[i]
     cum_exp += exp_spec[i]
     if i%5 == 0 or i == g/2:
         print("%2d-%2d : %5d  %7.1f" % (begin_group, i, cum_obs, cum_exp))
         cum_obs = cum_exp = 0
         begin_group = i+1


