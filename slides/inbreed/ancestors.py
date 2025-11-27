import datetime
year = datetime.datetime.now().year
gentime = 29 # length of a generation
print "Ancestors of a baby born in %d, assuming %d-year generations" % \
      (year, gentime)
print "%10s %10s %12s" % ("generation", "year", "ancestors")
a = 1
t = year
g = 0
while t > 1066:
    if g>0:
        print "%10d %10d %12d = %8.3g" % (g, t, a, a)
    a *= 2
    g += 1
    t -= gentime
print "%10d %10d %12d = %8.3g" % (g, t, a, a)
print """
During the Norman invasion (1066 AD) you had far
more ancestors than there were people on earth.
"""
