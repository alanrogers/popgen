# For graphics
from pylab import hist, show

# Dummy DNA sequence data set
data = ['GG', 'CG', 'GG', 'GG', 'CG', 'CG', 'CG', 'GG', 'GG', 'CC']

# Recode data so that data[i] is the number of copies of 'C' in
# genotype i.  "enumerate" was added recently to Python, so this
# may not work for you.
for i, y in enumerate(data):
    data[i] = y.count('C')

# The line below is self explanatory, so this comment is useless.
print("data:", data)

# Make a histogram (will not be visible until "show" executes)
hist(data)

# Tabulate counts
h = {}
for i in set(data):
    h[i] = data.count(i)

# To figure out the print statements below, see section 7.1 of the
# Python Tutorial.
print("h:", h)
print("%5s %5s" % ("Value", "Count"))
for i in [0,1,2]:
    print("%5d %5d" % (i, h[i]))

print()
n = len(data)
print("Sample size:", n)

# Convert counts into relative frequencies
for i in [0,1,2]:
    h[i] /= float(n)

print("%5s %-10s" % ("Value", "Proportion"))
for i in [0,1,2]:
    print("%5d %10.2f" % (i, h[i]))
print()

# Calculate mean from original data
m1 = sum(data)/float(n)

# Calculate mean from frequency distribution
m = 0.0
for i in [0,1,2]:
    m += i*h[i]
# Note: we don't have to divide by n.

print("Two versions of mean:", m1, m)
    
# Calculate variance from original data
v1 = 0.0
for x in data:
    v1 += (x - m)**2
v1 /= n

# Calculate variance using frequency distribution
v = 0.0
for i in [0,1,2]:
    v += h[i] * (i-m)**2

print("Two versions of variance:", v1, v)

# What happens to mean and variance if we double each
# entry in data?
for i, x in enumerate(data):
    data[i] = 2*x

print("Doubled data:", data)

m_dbl = sum(data)/float(n)
v_dbl = 0.0
for x in data:
    v_dbl += (x - m_dbl)**2
v_dbl /= n

print("Mean, var of doubled data:", m_dbl, v_dbl)

# Note that m_dbl == 2*m, and that v_dbl == 4*v

# Display histogram (generated above by hist) interactively
show()

    


