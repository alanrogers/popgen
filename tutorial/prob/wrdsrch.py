import os
from math import exp

target = "can"
npage = 30
ncounts = 1000
distr = ncounts*[0]

wordcount=matchcount=0
for dirpath, dirnames, fnames in os.walk("."):
    for fn in fnames:
        l = len(fn)
        if l < 5:
            continue
        suffix = fn[l-4:]
        #if suffix != ".tex" and suffix != ".txt":
        if fn[0] == '.':
            continue
        if suffix != ".tex":
            continue
        if fn[:3] == "fig":
            continue
        fn = os.path.join(dirpath, fn)
        #print "file", fn
        for line in open(fn):
            line = line.strip()
            words = line.split()
            for word in words:
                word = word.lower().rstrip(" ,;.:")
                if not word.isalpha():
                    continue
                if len(word) < 3:
                    continue
                #print "%-20s" % word,
                if word == target:
                    matchcount += 1
                    #print "match"
                #else:
                    #print "No match"
                wordcount += 1
                if wordcount >= npage:
                    if matchcount >= ncounts:
                        matchcount = ncounts-1
                    distr[matchcount] += 1
                    wordcount = matchcount = 0

sumx = sumxx = 0
totpages = 0
for x, n in enumerate(distr):
    sumx += x*n
    sumxx += x*x*n
    totpages += n

m = sumx / float(totpages)
v = sumxx/float(totpages) - m*m
print("Mean=%f Var=%f V/M=%f" % (m, v, v/m))

# Pr[x] = m**x * exp(-m) /factorial(x)
factorial = 1.0
p = exp(-m)
print("%4s %6s %8s" % ("x", "Obs", "Poisson"))
for x, n in enumerate(distr):
    if n > 0:
        print("%4d %6.4f %8.4f" % (x, n/float(totpages), p))
    if x >= 1:
        factorial *= x+1
    p *= m/float(factorial)
    
print("Based on %d copies of the word '%s'" % (sumx, target), end=' ')
print("spread across %d pages of size %d." % (totpages, npage))
print("%d words in all" % (npage*totpages))
