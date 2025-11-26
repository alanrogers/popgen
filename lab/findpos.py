from pgen import *
target = 136325116
hds = hapmap_dataset(hapmap_fname(99,'CEU'))
print("Searching for SNP at position", target)
ndx = hds.find_position(target)
print("Found SNP at position        ", hds[ndx].position)
