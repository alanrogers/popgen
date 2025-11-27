from pgen import bnldev

nRepl = 10000
twoN = 10000
s = 0.001   # selection for allele 2
h = 0.5

w11 = 1.0
w12 = 1.0 + h*s
w22 = 1.0 + s

nfixed = 0
for rep in range(nRepl):
    gen = 0
    q = 1.0/twoN
    while 0 < q < 1:
        gen += 1
        p = 1.0-q
        wbar = p*p * w11 + 2*p*q*w12 + q*q * w22
        qprime = q*(p*w12 + q*w22)/wbar
        q = bnldev(twoN, qprime)/float(twoN)
    if q == 1.0:
        nfixed += 1
print("s=%f 2N=%f fractionFixed=%f" % (s, twoN, nfixed/float(nRepl)))
print("fraction expected:", 2*h*s)    
    
