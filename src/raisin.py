#!/usr/bin/python
from math import exp

binwidth = 3

# Number of raisins in slices of raisin bread, counted by students in
# Anth/Biol 5221, University of Utah

today = "Sep 6, 2017"
x = 2*[8] + 3*[9] + 3*[10] + 2*[11] + 3*[12] + 3*[13] + 3*[14] \
  + 2*[15] + 3*[16] + 6*[17] + [18] + 3*[19] + [20,21]

#today = "Sept 6, 2013"
#x = [17,23,16,19,16,22,23,19,22,25,17,22,20,25,20,14,34,23,18,21,17,\
#     21,22,22,15,21,17,18,24,21,16,22]

#today = "Aug 28, 2009"
#x = [19,22,21,24,28,24,27,25,26,26,21,25,14,20,20,9,27,21,30,17,27,\
#     25,29,21,29,12,24,20,16,20,20,22,22,33,22,17,14,21,17,19,16]

N = len(x)
m = sum(x)/float(N)
v = sum([(x[i]-m)**2 for i in range(len(x))])/float(N-1)
print("Date:", today)
print("N=%d, Mean=%f, Var=%f, Max=%d" % (N, m, v, max(x)))

n = (1+max(x))*[0]
p = (1+max(x))*[0.0]

pval = exp(-m)
for i in range(max(x)):
    n[i] = x.count(i)
    p[i] = pval
    pval *= m/(i+1)

# Poisson fit
sumpois = 0.0
bins_got = sumdat = 0
for i in range(1,max(x)+1):
    sumdat += n[i]
    sumpois += p[i]*N
    bins_got += 1
    if bins_got == binwidth:
        s = int(sumpois+0.5)*['-'] # round to nearest int
        need = sumdat - len(s) + 1
        if need>0:
            s += need*[' ']
        assert len(s) > n[i]
        s[sumdat] = '*'
        s = ''.join(s)

        print("%2s-%2d: %s" % (i-binwidth+1,i, s))
        bins_got = sumdat = sumpois = 0

print("\nKey: ---- Poisson distribution w/ mean %f" % m)
print("        * Data")
